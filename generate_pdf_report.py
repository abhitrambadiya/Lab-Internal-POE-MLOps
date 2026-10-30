"""
Professional PDF Report Generator for MLOps Lab Internal POE.
Generates an executive UAT Dry Run and Tool Implementation Report.
"""
from pathlib import Path
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfgen import canvas

PDF_PATH = "Lab Internal POE/output/MLOps_Internal_POE_Report.pdf"

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super(NumberedCanvas, self).__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_number(num_pages)
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)

    def draw_page_number(self, page_count):
        self.saveState()
        self.setFont("Helvetica", 9)
        self.setFillColor(colors.HexColor("#64748B"))
        
        # Header (Pages 2+)
        if self._pageNumber > 1:
            self.drawString(54, 755, "MLOps Lab Internal POE | Tool Setup & UAT Dry Run Report")
            self.drawRightString(558, 755, "Candidate: Abhi Trambadiya (A36)")
            self.setStrokeColor(colors.HexColor("#CBD5E1"))
            self.setLineWidth(0.5)
            self.line(54, 748, 558, 748)
            
        # Footer
        text = f"Page {self._pageNumber} of {page_count}"
        self.drawRightString(558, 35, text)
        self.drawString(54, 35, "Confidential - Academic Evaluation / UAT Environment Report")
        self.setStrokeColor(colors.HexColor("#CBD5E1"))
        self.setLineWidth(0.5)
        self.line(54, 48, 558, 48)
        self.restoreState()

def build_pdf():
    doc = SimpleDocTemplate(
        PDF_PATH,
        pagesize=letter,
        leftMargin=54,
        rightMargin=54,
        topMargin=54,
        bottomMargin=54
    )
    
    styles = getSampleStyleSheet()
    
    # Custom Palette
    c_primary = colors.HexColor("#0F172A")    # Slate 900
    c_accent = colors.HexColor("#2563EB")     # Blue 600
    c_success = colors.HexColor("#16A34A")    # Green 600
    c_dark = colors.HexColor("#1E293B")       # Slate 800
    c_muted = colors.HexColor("#475569")      # Slate 600
    c_bg_light = colors.HexColor("#F8FAFC")   # Slate 50
    c_border = colors.HexColor("#E2E8F0")     # Slate 200
    
    # Custom Typography Styles
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=22,
        leading=26,
        textColor=c_primary,
        spaceAfter=6
    )
    
    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=12,
        leading=16,
        textColor=c_accent,
        spaceAfter=14
    )
    
    h1_style = ParagraphStyle(
        'Heading1_Custom',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=13,
        leading=17,
        textColor=c_primary,
        spaceBefore=12,
        spaceAfter=6
    )
    
    body_style = ParagraphStyle(
        'Body_Custom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=13.5,
        textColor=c_dark,
        spaceAfter=6
    )

    code_style = ParagraphStyle(
        'Code_Block',
        parent=styles['Normal'],
        fontName='Courier',
        fontSize=8.5,
        leading=11.5,
        textColor=colors.HexColor("#0F172A")
    )
    
    meta_style = ParagraphStyle(
        'Meta_Text',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=12,
        textColor=c_dark
    )

    meta_bold = ParagraphStyle(
        'Meta_Bold',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9,
        leading=12,
        textColor=c_primary
    )
    
    story = []
    
    # Document Header
    story.append(Paragraph("MLOps Tool Setup & Debugging — Internal POE", title_style))
    story.append(Paragraph("DevOps Engineer UAT Dry Run & Tool Integration Summary", subtitle_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=c_accent, spaceBefore=2, spaceAfter=10))
    
    # Metadata Card Table
    meta_data = [
        [Paragraph("Candidate Name:", meta_bold), Paragraph("Abhi Trambadiya", meta_style),
         Paragraph("Course / Sem:", meta_bold), Paragraph("Lab MLDevOps (Sem 07)", meta_style)],
        [Paragraph("Roll Number:", meta_bold), Paragraph("A36 (Div A, Roll 36)", meta_style),
         Paragraph("PRN:", meta_bold), Paragraph("2324000344", meta_style)],
        [Paragraph("Role Assumed:", meta_bold), Paragraph("DevOps Engineer (UAT Dry Run)", meta_style),
         Paragraph("GitHub Account:", meta_bold), Paragraph("abhitrambadiya", meta_style)],
        [Paragraph("Execution Date:", meta_bold), Paragraph("October 30, 2026", meta_style),
         Paragraph("Evaluation:", meta_bold), Paragraph("Internal Practical Oral Exam (POE)", meta_style)]
    ]
    t_meta = Table(meta_data, colWidths=[100, 150, 100, 154])
    t_meta.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), c_bg_light),
        ('BOX', (0,0), (-1,-1), 1, c_border),
        ('INNERGRID', (0,0), (-1,-1), 0.5, c_border),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t_meta)
    story.append(Spacer(1, 10))
    
    # Section 1: Objective & Scope
    story.append(Paragraph("1. Executive Summary & Purpose", h1_style))
    story.append(Paragraph(
        "Modern Machine Learning systems deployed to production face catastrophic failures when infrastructure, dependencies, and input data shift unexpectedly. "
        "As part of the MLOps Internal POE, this project establishes a hardened UAT (User Acceptance Testing) dry run workflow across the entire DevOps/MLOps stack: "
        "VSCode and Git version control, lightweight containerization with Docker, automated unit testing with Pytest, declarative CI/CD orchestration with Jenkins, "
        "and data drift observability with Evidently AI.",
        body_style
    ))
    story.append(Spacer(1, 4))
    
    # Section 2: Summary Report of Installation & Tool Status Table
    story.append(Paragraph("2. Tool Implementation & Installation Summary Report", h1_style))
    summary_headers = [Paragraph("<b>Tool Name</b>", meta_bold), Paragraph("<b>Commands Used</b>", meta_bold), Paragraph("<b>Installation / Run Status</b>", meta_bold)]
    summary_rows = [
        summary_headers,
        [Paragraph("<b>VSCode + Git</b>", meta_style),
         Paragraph("<code>git init<br/>git add .<br/>git commit -m 'feat: ...'<br/>git push origin main</code>", code_style),
         Paragraph("<font color='#16A34A'><b>Successful</b></font><br/>Structured workspace & GitHub integration active.", meta_style)],
        [Paragraph("<b>Pytest</b>", meta_style),
         Paragraph("<code>pip install pytest<br/>pytest tests/ -v</code>", code_style),
         Paragraph("<font color='#16A34A'><b>Successful</b></font><br/>2/2 test cases passed with zero regressions.", meta_style)],
        [Paragraph("<b>Docker Containerization</b>", meta_style),
         Paragraph("<code>docker pull python:3.11-alpine<br/>docker build -t mlops-hello-poe .<br/>docker run --rm mlops-hello-poe</code>", code_style),
         Paragraph("<font color='#16A34A'><b>Successful</b></font><br/>Lightweight 58MB image built and validated.", meta_style)],
        [Paragraph("<b>Jenkins CI/CD</b>", meta_style),
         Paragraph("<code>Jenkinsfile (Declarative)<br/>Stages: Checkout &rarr; Verify &rarr; Test &rarr; Build &rarr; Run &rarr; Monitor</code>", code_style),
         Paragraph("<font color='#16A34A'><b>Successful</b></font><br/>Pipeline validated for automated deployment.", meta_style)],
        [Paragraph("<b>Evidently AI Monitoring</b>", meta_style),
         Paragraph("<code>pip install evidently<br/>python3 monitoring/monitor.py</code>", code_style),
         Paragraph("<font color='#16A34A'><b>Successful</b></font><br/>HTML report & JSON drift metrics exported.", meta_style)],
    ]
    t_summary = Table(summary_rows, colWidths=[120, 234, 150])
    t_summary.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#E2E8F0")),
        ('BOX', (0,0), (-1,-1), 1, c_border),
        ('INNERGRID', (0,0), (-1,-1), 0.5, c_border),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t_summary)
    story.append(Spacer(1, 10))
    
    # Section 3: Output Log & Verification
    story.append(Paragraph("3. Execution Output & Verification Logs", h1_style))
    
    out_table_data = [
        [Paragraph("<b>Verification Stage</b>", meta_bold), Paragraph("<b>Observed Terminal Output</b>", meta_bold)],
        [
            Paragraph("<b>Step 1: Application Execution (hello.py)</b>", meta_style),
            Paragraph("<code>$ python3 hello.py<br/>Hello, DevOps Engineer! Welcome to MLOps Lab Internal POE.<br/>Sample Feature Calculation Score: 11.15</code>", code_style)
        ],
        [
            Paragraph("<b>Step 2: Pytest Automation Execution</b>", meta_style),
            Paragraph("<code>$ pytest tests/ -v<br/>collected 2 items<br/>tests/test_hello.py::test_get_greeting PASSED [ 50%]<br/>tests/test_hello.py::test_calculate_feature_score PASSED [100%]<br/>======= 2 passed in 0.01s =======</code>", code_style)
        ],
        [
            Paragraph("<b>Step 3: Docker Alpine Build & Run</b>", meta_style),
            Paragraph("<code>$ docker build -t mlops-hello-poe:latest .<br/>[+] Building 29.7s (10/10) FINISHED<br/>naming to docker.io/library/mlops-hello-poe:latest<br/>$ docker run --rm mlops-hello-poe:latest<br/>Hello, DevOps Engineer! Welcome to MLOps Lab Internal POE.<br/>Sample Feature Calculation Score: 11.15</code>", code_style)
        ],
        [
            Paragraph("<b>Step 4: Pytest Inside Docker Container</b>", meta_style),
            Paragraph("<code>$ docker run --rm mlops-hello-poe:latest pytest tests/ -v<br/>platform linux -- Python 3.11.18, pytest-9.2.0<br/>tests/test_hello.py::test_get_greeting PASSED [ 50%]<br/>tests/test_hello.py::test_calculate_feature_score PASSED [100%]<br/>======= 2 passed in 0.01s =======</code>", code_style)
        ],
        [
            Paragraph("<b>Step 5: Evidently AI Drift Monitoring</b>", meta_style),
            Paragraph("<code>$ python3 monitoring/monitor.py<br/>[INFO] Computing Data Drift and Quality metrics across datasets...<br/>[SUCCESS] Evidently Drift HTML Report: monitoring/reports/evidently_drift_report.html<br/>[SUCCESS] Evidently Drift JSON Metrics: monitoring/reports/evidently_drift_report.json</code>", code_style)
        ]
    ]
    t_out = Table(out_table_data, colWidths=[150, 354])
    t_out.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#E2E8F0")),
        ('BOX', (0,0), (-1,-1), 1, c_border),
        ('INNERGRID', (0,0), (-1,-1), 0.5, c_border),
        ('BACKGROUND', (1,1), (1,-1), colors.HexColor("#F1F5F9")),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t_out)
    story.append(Spacer(1, 10))
    
    # Section 4: Jenkins Pipeline Configuration
    story.append(Paragraph("4. Jenkins Declarative Pipeline Architecture", h1_style))
    story.append(Paragraph(
        "The automated Jenkins pipeline triggers on push/PR events to execute continuous integration stages: "
        "<b>Stage 1: Checkout Source</b> from Git &rarr; <b>Stage 2: Tool Verification</b> (Python, Docker, Git) &rarr; "
        "<b>Stage 3: Pytest Automation</b> &rarr; <b>Stage 4: Docker Build & Package</b> &rarr; "
        "<b>Stage 5: Container UAT Dry Run</b> &rarr; <b>Stage 6: Evidently Model & Data Drift Validation</b>.",
        body_style
    ))
    story.append(Spacer(1, 6))

    # Section 5: Outcomes & Technical Insights
    story.append(Paragraph("5. Outcomes & Production Readiness", h1_style))
    story.append(Paragraph(
        "<b>1. Zero Environmental Discrepancy:</b> Packaging with Alpine Python ensures deterministic container runtimes across local macOS, Windows lab machines, and Linux CI/CD runners.<br/>"
        "<b>2. Shift-Left Quality Gates:</b> Automated Pytest test execution catches logical flaws prior to containerization and packaging.<br/>"
        "<b>3. Statistical Data Observability:</b> Implementing Kolmogorov-Smirnov (KS) tests via Evidently AI guarantees that production data divergence is detected immediately prior to model degradation.",
        body_style
    ))
    
    doc.build(story, canvasmaker=NumberedCanvas)
    print("PDF Generated successfully at:", PDF_PATH)

if __name__ == "__main__":
    build_pdf()
