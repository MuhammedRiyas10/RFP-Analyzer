# Electrical RFP Analyzer - Enterprise Edition ⚡📄

An AI-powered SaaS platform designed to automate the analysis of Electrical Request for Proposals (RFPs) and generate professional bids instantly. Built for the Tech Hackathon.

## 🚀 Key Features

### 1. **Intelligent Document Analysis**
-   **Multi-Format Support**: Upload PDF documents or images (PNG/JPG).
-   **OCR Integration**: Automatically extracts text from scanned files using Tesseract OCR.
-   **AI Classification**: Detects if the uploaded document is a valid Electrical RFP.

### 2. **Human-in-the-Loop (HITL) Workflow**
-   **Smart Interception**: The system pauses after analyzing the scope to detect missing information (Location, Timeline, Materials).
-   **Review Dashboard**: Users can verify and correct the extracted scope *before* the costly proposal generation step.
-   **Interactive Editing**: Edit JSON material lists and compliance requirements directly in the UI.

### 3. **Enterprise-Grade Dashboard**
-   **Glassmorphism UI**: Modern, clean interface with animated loading states ("Thinking" steps).
-   **Live Preview**: View the generated proposal in a "Paper" layout exactly as it will appear in the PDF.
-   **Scope & Cost Breakdown**: Visual cards showing detected scope items and calculated financial estimates.

### 4. **Instant Proposal Generation**
-   **One-Click PDF**: Download a client-ready PDF proposal.
-   **Professional Formatting**: Includes cover page, dynamic headers/footers, and clean typography.
-   **Client-Side Rendering**: High-fidelity conversion using `html2pdf.js`.

---

## 🛠️ Technology Stack

-   **Backend**: Django (Python)
-   **AI Orchestration**: LangChain (Custom Agents: Classifier, Scope, Cost, Proposal)
-   **Frontend**: Tailwind CSS, HTML5, JavaScript
-   **PDF Engine**: `html2pdf.js` + `marked.js`
-   **OCR**: Tesseract + Pillow

---

## 📦 Installation & Setup

1.  **Clone the Repository**
    ```bash
    git clone https://github.com/yourusername/electrical-rfp-analyzer.git
    cd electrical-rfp-analyzer
    ```

2.  **Create Virtual Environment**
    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # Mac/Linux
    source venv/bin/activate
    ```

3.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Database Migrations**
    ```bash
    python manage.py migrate
    ```

5.  **Run the Server**
    ```bash
    python manage.py runserver
    ```

6.  **Access the App**
    Open [http://localhost:8000](http://localhost:8000) in your browser.

---

## 🔄 Workflow Diagram

1.  **Upload**: User uploads an RFP PDF.
2.  **Analyze (Part 1)**: Agent extracts Scope & Requirements.
3.  **Verify (HITL)**: If critical info is missing, user is prompted to confirm.
4.  **Estimate (Part 2)**: Agent calculates Labor & Material costs based on confirmed scope.
5.  **Generate**: Final Proposal is created in Markdown -> Rendered to HTML -> Exportable to PDF.

---

## 📝 License

Developed for Tech Hackathon 2024. All rights reserved.
