from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from agents.orchestrator import RFPOrchestrator
from core.ocr_utils import extract_text_with_ocr
import markdown

from io import BytesIO
from PIL import Image
import pytesseract


def upload_rfp(request):
    if request.method == "POST":

        orchestrator = RFPOrchestrator()

        # ----------------------------
        # CASE 1: Confirmation Step (User approved/edited scope)
        # ----------------------------
        if request.POST.get("confirm_generation"):
            import json
            
            # Reconstruct scope from form data
            materials_json = request.POST.get("materials_json", "[]")
            try:
                materials_data = json.loads(materials_json)
            except:
                materials_data = []

            # Reconstruct list from textareas (newline separated)
            special_reqs = [x.strip() for x in request.POST.get("special_requirements", "").split("\n") if x.strip()]
            compliance_reqs = [x.strip() for x in request.POST.get("compliance_requirements", "").split("\n") if x.strip()]

            scope_data = {
                "project_type": request.POST.get("project_type"),
                "location": request.POST.get("location"),
                "timeline_months": int(request.POST.get("timeline_months", 0)),
                "materials_required": materials_data,
                "special_requirements": special_reqs,
                "compliance_requirements": compliance_reqs
            }

            # Run Part 2: Cost -> Proposal
            result = orchestrator.generate_from_scope(scope_data)
            
            # Format Markdown
            if "proposal" in result:
                result["proposal_html"] = markdown.markdown(
                    result["proposal"],
                    extensions=["extra", "tables"]
                )
            
            return render(request, "result.html", {"result": result})

        # ----------------------------
        # CASE 2: Initial Upload (File or Text)
        # ----------------------------
        file = request.FILES.get("rfp_file")
        text_input = request.POST.get("rfp_text")
        text = None

        if file:
            filename = file.name.lower()
            if filename.endswith(".pdf"):
                text = extract_text_with_ocr(file)
            elif filename.endswith((".png", ".jpg", ".jpeg")):
                image = Image.open(file)
                text = pytesseract.image_to_string(image)
            else:
                text = file.read().decode("utf-8")
        elif text_input and text_input.strip():
            text = text_input
        else:
            return render(request, "upload.html", {
                "error": "Please upload a file or enter text."
            })

        # Run Part 1: Classify -> Scope
        partial_result = orchestrator.extract_scope_only(text)

        if "error" in partial_result:
             return render(request, "result.html", {"result": partial_result})

        scope = partial_result.get("scope", {})
        
        # ----------------------------
        # HITL CHECK: Missing Information?
        # ----------------------------
        missing_fields = []
        if not scope.get("location") or scope.get("location") == "Unknown":
            missing_fields.append("Location")
        if not scope.get("timeline_months"):
            missing_fields.append("Timeline")
        if not scope.get("materials_required"):
            missing_fields.append("Materials")
        if not scope.get("compliance_requirements"):
            missing_fields.append("Compliance")

        # If we have missing fields, INTERCEPT flow and show confirmation
        if missing_fields:
            import json
            # Prepare data for confirm.html
            materials_json = json.dumps(scope.get("materials_required", []), indent=2)
            
            return render(request, "confirm.html", {
                "scope": scope,
                "materials_json": materials_json,
                "missing_fields": missing_fields
            })

        # If Clean: Proceed to Part 2 immediately
        result = orchestrator.generate_from_scope(scope)

        if "proposal" in result:
            result["proposal_html"] = markdown.markdown(
                result["proposal"],
                extensions=["extra", "tables"]
            )

        return render(request, "result.html", {"result": result})

    return render(request, "upload.html")


# ------------------------------------------
# NEW VIEW: Download Proposal as PDF
# ------------------------------------------
