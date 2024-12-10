    # def generate_footer(self, canvas, doc):
    #     # Dessinez votre footer ici
    #     footer_text = "Scan Report"
    #     canvas.saveState()
    #     canvas.setFont("Helvetica", 10)
    #     canvas.drawString(inch, inch, footer_text)
    #     canvas.drawString(9*inch, inch, "Etna module 168H")
    #     canvas.restoreState()

    # def generate_frames(self, doc):
    #     # Dessinez la table sur le canvas à la position spécifiée pour le format paysage
    #     if doc.pagesize[0] > doc.pagesize[1]:  # paysage
    #         content_frame = Frame(-inch, inch, 9.5 * inch, 7 * inch, id='ContentFrame', showBoundary=1)
    #         footer_frame = Frame(-inch, 0.5 * inch, 9.5 * inch, 0.5 * inch, id='FooterFrame', showBoundary=1)
    #     else:  # portrait
    #         content_frame = Frame(inch, inch, 7 * inch, 9 * inch, id='ContentFrame', showBoundary=1)
    #         footer_frame = Frame(inch, 0.5 * inch, 7 * inch, 0.5 * inch, id='FooterFrame', showBoundary=1)
        
    #     return [content_frame, footer_frame]
    