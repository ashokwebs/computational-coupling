import os
import re
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, HRFlowable, Table, TableStyle, KeepTogether
)
from reportlab.pdfgen import canvas

TEX_MAIN = "/home/charizard/computational-coupling/paper/main.tex"
PDF_OUT = "/home/charizard/computational-coupling/paper/output/paper.pdf"

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, page_count):
        self.saveState()
        self.setFont("Helvetica-Bold", 8)
        self.setFillColor(colors.HexColor("#333333"))
        if self._pageNumber > 1:
            self.drawString(54, 11 * 72 - 36, "A Theory of Computational Coupling Between Intelligent Systems")
            self.setStrokeColor(colors.HexColor("#2E75B6"))
            self.setLineWidth(0.75)
            self.line(54, 11 * 72 - 40, 8.5 * 72 - 54, 11 * 72 - 40)
        
        self.setFont("Helvetica", 8)
        self.drawRightString(8.5 * 72 - 54, 30, f"Page {self._pageNumber} of {page_count}")
        self.drawString(54, 30, "Ashok Pasala (VIT-AP University) — Working Draft v0.2.0")
        self.setStrokeColor(colors.HexColor("#E0E0E0"))
        self.setLineWidth(0.5)
        self.line(54, 40, 8.5 * 72 - 54, 40)
        self.restoreState()

def clean_latex_math(text):
    """Converts LaTeX formatting into clean HTML/ReportLab markup."""
    # Bold, Italic, Code
    text = re.sub(r'\\textbf\{([^}]+)\}', r'<b>\1</b>', text)
    text = re.sub(r'\\emph\{([^}]+)\}', r'<i>\1</i>', text)
    text = re.sub(r'\\textit\{([^}]+)\}', r'<i>\1</i>', text)
    text = re.sub(r'\\texttt\{([^}]+)\}', r'<font face="Courier">\1</font>', text)
    
    # Common math symbols & commands
    text = re.sub(r'\\mathrm\{([^}]+)\}', r'<b>\1</b>', text)
    text = re.sub(r'\\mathcal\{([^}]+)\}', r'<i>\1</i>', text)
    text = re.sub(r'\\mathbb\{([^}]+)\}', r'<b>\1</b>', text)
    text = re.sub(r'\\text\{([^}]+)\}', r'\1', text)

    # Greek letters & math symbols
    math_map = {
        r'\sup': 'sup', r'\min': 'min', r'\max': 'max',
        r'\alpha': 'α', r'\beta': 'β', r'\Delta': 'Δ', r'\delta': 'δ',
        r'\tau': 'τ', r'\phi': 'φ', r'\psi': 'ψ', r'\Phi': 'Φ',
        r'\mu': 'μ', r'\varepsilon': 'ε', r'\epsilon': 'ε',
        r'\in': '∈', r'\notin': '∉', r'\to': '→', r'\longmapsto': '⟼',
        r'\cdot': '·', r'\dots': '...', r'\vert': '|', r'\mid': '|',
        r'\le': '≤', r'\ge': '≥', r'\neq': '≠', r'\approx': '≈',
        r'\partial': '∂', r'\infty': '∞', r'\sum': '∑', r'\prod': '∏'
    }
    for cmd, sym in math_map.items():
        text = text.replace(cmd, sym)

    # Remove remaining backslashes from simple latex brackets/formatting
    text = re.sub(r'\\cite\{([^}]+)\}', r'[\1]', text)
    text = re.sub(r'\\ref\{([^}]+)\}', r'\1', text)
    text = re.sub(r'\\noindent', '', text)
    text = re.sub(r'\\\[', '', text)
    text = re.sub(r'\\\]', '', text)
    text = re.sub(r'\\\(', '', text)
    text = re.sub(r'\\\)', '', text)
    text = text.replace('$', '')
    
    # Clean up multi-space
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def compile_tex_to_pdf():
    os.makedirs(os.path.dirname(PDF_OUT), exist_ok=True)
    doc = SimpleDocTemplate(
        PDF_OUT, pagesize=letter,
        leftMargin=54, rightMargin=54, topMargin=54, bottomMargin=54
    )
    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        'TexTitle', parent=styles['Title'], fontName='Helvetica-Bold',
        fontSize=18, leading=22, textColor=colors.HexColor("#1F4E78"), spaceAfter=6, alignment=1
    )
    subtitle_style = ParagraphStyle(
        'TexSubTitle', parent=styles['Normal'], fontName='Helvetica-Bold',
        fontSize=12, leading=16, textColor=colors.HexColor("#2E75B6"), spaceAfter=10, alignment=1
    )
    author_style = ParagraphStyle(
        'TexAuthor', parent=styles['Normal'], fontName='Helvetica',
        fontSize=10, leading=14, textColor=colors.HexColor("#333333"), spaceAfter=14, alignment=1
    )
    h1_style = ParagraphStyle(
        'TexH1', parent=styles['Heading1'], fontName='Helvetica-Bold',
        fontSize=13, leading=16, textColor=colors.HexColor("#1F4E78"), spaceBefore=14, spaceAfter=6, keepWithNext=True
    )
    h2_style = ParagraphStyle(
        'TexH2', parent=styles['Heading2'], fontName='Helvetica-Bold',
        fontSize=11, leading=14, textColor=colors.HexColor("#2E75B6"), spaceBefore=10, spaceAfter=4, keepWithNext=True
    )
    body_style = ParagraphStyle(
        'TexBody', parent=styles['Normal'], fontName='Helvetica',
        fontSize=9.5, leading=14, textColor=colors.HexColor("#111111"), spaceAfter=6
    )
    abstract_style = ParagraphStyle(
        'TexAbstract', parent=styles['Normal'], fontName='Helvetica-Oblique',
        fontSize=9, leading=13.5, textColor=colors.HexColor("#222222"), leftIndent=16, rightIndent=16, spaceAfter=12
    )
    bullet_style = ParagraphStyle(
        'TexBullet', parent=body_style, leftIndent=14, bulletIndent=4, spaceAfter=4
    )
    box_title_style = ParagraphStyle(
        'BoxTitle', parent=styles['Normal'], fontName='Helvetica-Bold',
        fontSize=10, leading=13, textColor=colors.HexColor("#1F4E78"), spaceAfter=3
    )
    box_body_style = ParagraphStyle(
        'BoxBody', parent=styles['Normal'], fontName='Helvetica',
        fontSize=9, leading=13, textColor=colors.HexColor("#222222")
    )

    story = []
    
    with open(TEX_MAIN, "r", encoding="utf-8") as f:
        content = f.read()

    # Title & Header
    story.append(Paragraph("A Theory of Computational Coupling Between Intelligent Systems", title_style))
    story.append(Paragraph("Toward a General Foundation for Brain-to-Brain Communication", subtitle_style))
    story.append(Paragraph("<b>Ashok Pasala</b> &nbsp;|&nbsp; VIT-AP University &nbsp;|&nbsp; <i>Working Draft v0.2.0 (July 23, 2026)</i>", author_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor("#1F4E78"), spaceBefore=0, spaceAfter=12))

    # Parse Sections
    raw_blocks = content.split('\n\n')
    in_abstract = False

    for block in raw_blocks:
        block = block.strip()
        if not block:
            continue
        if r'\documentclass' in block or r'\usepackage' in block or r'\maketitle' in block or r'\begin{document}' in block or r'\end{document}' in block:
            continue

        if r'\begin{abstract}' in block:
            in_abstract = True
            text = block.replace(r'\begin{abstract}', '').replace(r'\end{abstract}', '').strip()
            text = clean_latex_math(text)
            story.append(Paragraph("<b>ABSTRACT</b>", h2_style))
            story.append(Paragraph(text, abstract_style))
            story.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor("#CCCCCC"), spaceBefore=4, spaceAfter=12))
            in_abstract = False
            continue

        # Section Headers
        if r'\section{' in block:
            m = re.search(r'\\section\*?\{([^}]+)\}', block)
            if m:
                story.append(Paragraph(m.group(1), h1_style))
                continue

        if r'\subsection{' in block:
            m = re.search(r'\\subsection\*?\{([^}]+)\}', block)
            if m:
                story.append(Paragraph(m.group(1), h2_style))
                continue

        # Predictions / Definitions Boxes
        if r'\begin{prediction}' in block or r'\begin{definitionbox}' in block:
            box_type = "PREDICTION" if r'\begin{prediction}' in block else "DEFINITION"
            m_title = re.search(r'\[([^\]]+)\]', block)
            box_label = f"<b>{box_type}: {m_title.group(1)}</b>" if m_title else f"<b>{box_type}</b>"
            
            clean_body = re.sub(r'\\begin\{(prediction|definitionbox)\}(\[[^\]]+\])?', '', block)
            clean_body = re.sub(r'\\end\{(prediction|definitionbox)\}', '', clean_body).strip()
            clean_body = clean_latex_math(clean_body)
            
            # Create shrunken callout box table
            box_data = [[Paragraph(box_label, box_title_style)], [Paragraph(clean_body, box_body_style)]]
            box_table = Table(box_data, colWidths=[500])
            box_table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor("#F0F4F8")),
                ('BOX', (0, 0), (-1, -1), 1, colors.HexColor("#2E75B6")),
                ('PADDING', (0, 0), (-1, -1), 8),
                ('TOPPADDING', (0, 0), (-1, 0), 6),
                ('BOTTOMPADDING', (0, -1), (-1, -1), 6),
            ]))
            story.append(Spacer(1, 4))
            story.append(box_table)
            story.append(Spacer(1, 6))
            continue

        # Itemize / Enumerate
        if r'\begin{itemize}' in block or r'\begin{enumerate}' in block:
            items = re.findall(r'\\item\s+([^\n]+(?:\n[^\n]+)*)', block)
            for item in items:
                clean_item = clean_latex_math(item)
                story.append(Paragraph(f"• {clean_item}", bullet_style))
            continue

        # Paragraph text
        clean_p = clean_latex_math(block)
        if clean_p:
            story.append(Paragraph(clean_p, body_style))

    doc.build(story, canvasmaker=NumberedCanvas)
    print("Paper compiled cleanly to PDF:", PDF_OUT)

if __name__ == "__main__":
    compile_tex_to_pdf()
