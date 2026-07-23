import os
import re
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable
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
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#555555"))
        if self._pageNumber > 1:
            self.drawString(54, 11 * 72 - 36, "A Theory of Computational Coupling Between Intelligent Systems")
            self.setStrokeColor(colors.HexColor("#CCCCCC"))
            self.setLineWidth(0.5)
            self.line(54, 11 * 72 - 40, 8.5 * 72 - 54, 11 * 72 - 40)
        self.drawRightString(8.5 * 72 - 54, 30, f"Page {self._pageNumber} of {page_count}")
        self.drawString(54, 30, "Ashok Pasala (VIT-AP University) — Working Draft v0.2.0")
        self.setStrokeColor(colors.HexColor("#CCCCCC"))
        self.setLineWidth(0.5)
        self.line(54, 40, 8.5 * 72 - 54, 40)
        self.restoreState()

def compile_tex_to_pdf():
    os.makedirs(os.path.dirname(PDF_OUT), exist_ok=True)
    doc = SimpleDocTemplate(PDF_OUT, pagesize=letter, leftMargin=54, rightMargin=54, topMargin=54, bottomMargin=54)
    styles = getSampleStyleSheet()

    body_style = ParagraphStyle('TexBody', parent=styles['Normal'], fontName='Helvetica', fontSize=9.5, leading=13.5, textColor=colors.HexColor("#111111"), spaceAfter=6)
    title_style = ParagraphStyle('TexTitle', parent=styles['Title'], fontName='Helvetica-Bold', fontSize=16, leading=20, textColor=colors.HexColor("#000000"), spaceAfter=6, alignment=1)
    author_style = ParagraphStyle('TexAuthor', parent=styles['Normal'], fontName='Helvetica', fontSize=10, leading=14, textColor=colors.HexColor("#333333"), spaceAfter=12, alignment=1)
    h1_style = ParagraphStyle('TexH1', parent=styles['Heading1'], fontName='Helvetica-Bold', fontSize=13, leading=16, textColor=colors.HexColor("#1F4E78"), spaceBefore=12, spaceAfter=4, keepWithNext=True)
    h2_style = ParagraphStyle('TexH2', parent=styles['Heading2'], fontName='Helvetica-Bold', fontSize=11, leading=14, textColor=colors.HexColor("#2E75B6"), spaceBefore=8, spaceAfter=3, keepWithNext=True)
    abstract_style = ParagraphStyle('TexAbstract', parent=styles['Normal'], fontName='Helvetica-Oblique', fontSize=9, leading=13, textColor=colors.HexColor("#222222"), leftIndent=18, rightIndent=18, spaceAfter=10)
    bullet_style = ParagraphStyle('TexBullet', parent=body_style, leftIndent=14, bulletIndent=4, spaceAfter=3)

    story = []
    with open(TEX_MAIN, "r", encoding="utf-8") as f:
        content = f.read()

    lines = content.split('\n')
    in_abstract = False

    for line in lines:
        line = line.strip()
        if not line:
            continue
        if line.startswith(r'\begin{document}') or line.startswith(r'\maketitle') or line.startswith(r'\documentclass') or line.startswith(r'\usepackage'):
            continue
        if line.startswith(r'\end{document}'):
            break
        if line.startswith(r'\begin{abstract}'):
            in_abstract = True
            continue
        if line.startswith(r'\end{abstract}'):
            in_abstract = False
            continue

        text = line
        text = re.sub(r'\\title\{([^}]+)\}', r'TITLE:\1', text)
        text = re.sub(r'\\author\{([^}]+)\}', r'AUTHOR:\1', text)
        text = re.sub(r'\\section\{([^}]+)\}', r'H1:\1', text)
        text = re.sub(r'\\subsection\{([^}]+)\}', r'H2:\1', text)
        text = re.sub(r'\\textbf\{([^}]+)\}', r'<b>\1</b>', text)
        text = re.sub(r'\\emph\{([^}]+)\}', r'<i>\1</i>', text)
        text = re.sub(r'\\textit\{([^}]+)\}', r'<i>\1</i>', text)
        text = re.sub(r'\\cite\{([^}]+)\}', r'[Citation: \1]', text)
        text = re.sub(r'\\ref\{([^}]+)\}', r'\1', text)
        text = re.sub(r'\\noindent', '', text)
        text = re.sub(r'\\[a-zA-Z]+', '', text)

        if text.startswith('TITLE:'):
            story.append(Paragraph("A Theory of Computational Coupling Between Intelligent Systems", title_style))
        elif text.startswith('H1:'):
            story.append(Paragraph(text[3:], h1_style))
        elif text.startswith('H2:'):
            story.append(Paragraph(text[3:], h2_style))
        elif text.startswith(r'\item'):
            item_text = text[5:].strip()
            story.append(Paragraph(f"• {item_text}", bullet_style))
        elif in_abstract:
            story.append(Paragraph(text, abstract_style))
        else:
            story.append(Paragraph(text, body_style))

    doc.build(story, canvasmaker=NumberedCanvas)
    print("Paper compiled successfully to:", PDF_OUT)

if __name__ == "__main__":
    compile_tex_to_pdf()
