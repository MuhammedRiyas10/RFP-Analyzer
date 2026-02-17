from django.shortcuts import render
from agents.orchestrator import RFPOrchestrator
import pdfplumber


def upload_rfp(request):
    if request.method == "POST":

        file = request.FILES.get("rfp_file")
        text_input = request.POST.get("rfp_text")

        text = None

        # Case 1: File uploaded
        if file:
            if file.name.endswith(".pdf"):
                with pdfplumber.open(file) as pdf:
                    text = "\n".join(
                        page.extract_text() or "" for page in pdf.pages
                    )
            else:
                text = file.read().decode("utf-8")

        # Case 2: Text manually entered
        elif text_input and text_input.strip():
            text = text_input

        else:
            return render(request, "upload.html", {
                "error": "Please upload a file or enter text."
            })

        orchestrator = RFPOrchestrator()
        result = orchestrator.run(text)

        return render(request, "result.html", {"result": result})

    return render(request, "upload.html")
