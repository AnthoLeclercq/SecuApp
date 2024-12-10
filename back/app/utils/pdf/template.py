from reportlab.platypus import Frame, PageTemplate
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from utils.pdf.header import Header
from utils.pdf.footer import Footer

class PdfTemplate:
    def create_page_template(title):
        header = Header(width=letter[0], height=0.75 * inch, title=title)
        footer = Footer(width=letter[0], height=0.75 * inch)

        content_frame = Frame(
            x1=0.75 * inch,
            y1=0.75 * inch,
            width=letter[0] - 1.5 * inch,
            height=letter[1] - 1.5 * inch,
            leftPadding=0,
            bottomPadding=0,
            rightPadding=0,
            topPadding=0,
            showBoundary=0
        )

        page_template = PageTemplate(id='report', frames=[content_frame], onPage=[header, footer])

        return page_template