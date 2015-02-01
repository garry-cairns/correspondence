# -*- coding: utf-8 -*-
import sys
import datetime
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.platypus import (
        Image,
        Paragraph,
        SimpleDocTemplate,
        Spacer,
        Table,
    )
from letter_design import STYLES


class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        """Constructor"""
        canvas.Canvas.__init__(self, *args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        """add page info to each page (page x of y)"""
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_number(num_pages)
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)

    def draw_page_number(self, page_count):
        # Change the position of this to wherever you want the page number to be
        self.drawRightString(
                195 * mm,
                15 * mm,
                "Page %d of %d" % (self._pageNumber, page_count)
            )


class LetterCanvas(object):
    def __init__(self, body_text):
        """Constructor"""
        self.letter_text = letter_text
        self.pagesize = A4
        self.width, self.height = self.pagesize

    def run(self):
        """
        Run the report
        """
        self.doc = SimpleDocTemplate(
                "form_letter.pdf",
                rightMargin=15*mm,
                leftMargin=15*mm,
                topMargin=20*mm,
                bottomMargin=30*mm,
                pagesize=self.pagesize
            )
        self.elements = [Spacer(1, 67*mm)]
        self.insert_content()
        self.doc.build(
                self.elements,
                onFirstPage=self._first_page,
                onLaterPages=self._subsequent_pages,
                canvasmaker=NumberedCanvas
            )

    @staticmethod
    def _first_page(canvas, doc):
        """
        Defines layout for the first page of our letter.
        """
        # Save the state of our canvas so we can draw on it
        canvas.saveState()

        # Logo block
        logo = Image('http://upload.wikimedia.org/wikipedia/commons/9/9a/PNG_transparency_demonstration_2.png', width=70*mm, height=50*mm)
        logo.wrapOn(canvas, doc.width/2.0, doc.height)
        logo.drawOn(canvas, 15*mm, 232*mm)

        # Return address block
        ptext = """Return<br/>
        Address1<br/>
        Address2<br/>
        Address3<br/>
        Address4<br/>
        Postcode"""
        p = Paragraph(ptext, STYLES['ReturnAddress'])
        p.wrapOn(canvas, doc.width/3.0, doc.height)
        p.drawOn(canvas, 130*mm, 232*mm)

        # Recipient address block
        ptext = """<font size=12>Recipient<br/>
        Address1<br/>
        Address2<br/>
        Address3<br/>
        Address4<br/>
        Postcode</font>"""
        p = Paragraph(ptext, STYLES['Normal'])
        p.wrapOn(canvas, doc.width-300, doc.height)
        p.drawOn(canvas, 15*mm, 197*mm)

        # Footer
        footer = Paragraph('Return address, Where we live, City, Postcode', STYLES['Normal'])
        w, h = footer.wrap(doc.width, doc.bottomMargin)
        footer.drawOn(canvas, doc.leftMargin, h)

        # Release the canvas
        canvas.restoreState()

    @staticmethod
    def _subsequent_pages(canvas, doc):
        """
        Defines layout for all pages of our letter but the first.
        """
        # Save the state of our canvas so we can draw on it
        canvas.saveState()

        # Header
        header = Paragraph('Letter type', STYLES['Normal'])
        w, h = header.wrap(doc.width, doc.topMargin)
        header.drawOn(canvas, doc.leftMargin, doc.height + doc.topMargin + doc.bottomMargin - h*mm)

        # Footer
        footer = Paragraph('Return address, Where we live, City, Postcode', STYLES['Normal'])
        w, h = footer.wrap(doc.width, doc.bottomMargin-(15*mm))
        footer.drawOn(canvas, doc.leftMargin, h)

        # Release the canvas
        canvas.restoreState()

    def insert_content(self):
        """
        Inserts the flowable elements into our letter.
        """
        # Draw things on the PDF. Here's where the PDF generation happens.
        # See the ReportLab documentation for full list of functionality.

        letter_text = [
            'Donec nec nunc eu ante luctus sodales eu ac massa. Duis id auctor sapien. Sed vel faucibus sem. Suspendisse potenti. Proin ut augue condimentum, semper leo sed, laoreet odio. Nam lobortis vel elit sit amet egestas. Vestibulum congue nisi non semper sollicitudin.',
            ]

        self.elements.append(Paragraph(datetime.datetime.now().strftime("%d %B %y"), STYLES['DateLine']))
        self.elements.append(Paragraph('Letter title', STYLES['LetterTitle']))
        self.elements.append(Paragraph('Dear sir or madam', STYLES['Salutation']))
        for i, par in enumerate(lipsum):
            self.elements.append(Paragraph(par, STYLES['LetterBody']))
        self.elements.append(Paragraph('Yours sincerely', STYLES['Salutation']))
        self.elements.append(Paragraph('A Person', STYLES['Signature']))
        self.elements.append(Paragraph('Case officer', STYLES['SignatoryTitle']))
