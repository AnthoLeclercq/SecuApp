from reportlab.platypus.flowables import Flowable
from reportlab.lib.units import inch
from datetime import datetime

class Footer(Flowable):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height

    def draw(self):
        self.canv.setFont("Helvetica", 9)
        self.canv.drawString(inch, 0.75 * inch, f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
