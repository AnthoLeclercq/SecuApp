from reportlab.platypus.flowables import Flowable
from reportlab.lib.units import inch

class Header(Flowable):
    def __init__(self, width, height, title):
        super().__init__()
        self.width = width
        self.height = height
        self.title = title

    def draw(self):
        self.canv.setFont("Helvetica-Bold", 16)
        self.canv.drawString(inch, self.height - 0.5 * inch, self.title)