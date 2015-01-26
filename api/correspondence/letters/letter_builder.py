# -*- coding: utf-8 -*-
import sys
import datetime
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import (
        Image,
        Paragraph,
        SimpleDocTemplate,
        Spacer,
        Table,
    )
from reportlab.platypus.tables import TableStyle


class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
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


class MyPrint(object):
    def __init__(self):
        self.pagesize = A4
        self.width, self.height = self.pagesize

    @staticmethod
    def _first_page(canvas, doc):
        # Save the state of our canvas so we can draw on it
        canvas.saveState()
        styles = getSampleStyleSheet()

        # Footer
        footer = Paragraph('Return address, Where we live, City, Postcode', styles['Normal'])
        w, h = footer.wrap(doc.width, doc.bottomMargin)
        footer.drawOn(canvas, doc.leftMargin, h)

        # Release the canvas
        canvas.restoreState()

    @staticmethod
    def _subsequent_pages(canvas, doc):
        # Save the state of our canvas so we can draw on it
        canvas.saveState()
        styles = getSampleStyleSheet()

        # Header
        header = Paragraph('Letter type', styles['Normal'])
        w, h = header.wrap(doc.width, doc.topMargin)
        header.drawOn(canvas, doc.leftMargin, doc.height + doc.topMargin + doc.bottomMargin - h*mm)

        # Footer
        footer = Paragraph('Return address, Where we live, City, Postcode', styles['Normal'])
        w, h = footer.wrap(doc.width, doc.bottomMargin-(15*mm))
        footer.drawOn(canvas, doc.leftMargin, h)

        # Release the canvas
        canvas.restoreState()

    def print_lipsum(self):
        doc = SimpleDocTemplate(
                "form_letter.pdf",
                rightMargin=15*mm,
                leftMargin=15*mm,
                topMargin=20*mm,
                bottomMargin=30*mm,
                pagesize=self.pagesize
            )

        # Our container for 'Flowable' objects
        elements = []

        # Get pre-made styles and add to them
        styles = getSampleStyleSheet()
        styles.add(
                ParagraphStyle(
                    name='DateLine',
                    parent=styles['Normal'],
                    spaceBefore=30*mm,
                    fontSize=12,
                )
            )
        styles.add(
                ParagraphStyle(
                    name='LetterTitle',
                    parent=styles['Normal'],
                    spaceBefore=15*mm,
                    fontName='Helvetica-Bold',
                    fontSize=12,
                )
            )
        styles.add(
                ParagraphStyle(
                    name='Salutation',
                    parent=styles['Normal'],
                    spaceBefore=10*mm,
                    spaceAfter=10*mm,
                    fontSize=12,
                )
            )
        styles.add(
                ParagraphStyle(
                    name='LetterBody',
                    parent=styles['Normal'],
                    spaceAfter=3*mm,
                    fontSize=12,
                    leading=14,
                )
            )
        styles.add(
                ParagraphStyle(
                    name='Signature',
                    parent=styles['Normal'],
                    spaceBefore=30*mm,
                    spaceAfter=15*mm,
                    fontSize=12,
                )
            )
        styles.add(
                ParagraphStyle(
                    name='SignatoryTitle',
                    parent=styles['Normal'],
                    spaceBefore=30*mm,
                    spaceAfter=15*mm,
                    fontSize=12,
                )
            )

        # Draw things on the PDF. Here's where the PDF generation happens.
        # See the ReportLab documentation for full list of functionality.

        # Logo block
        logo = Image('http://upload.wikimedia.org/wikipedia/commons/thumb/4/47/PNG_transparency_demonstration_1.png/280px-PNG_transparency_demonstration_1.png')
        logo.drawWidth = 70*mm
        logo.drawHeight = 50*mm

        # create recipient address
        address = """Jack Spratt\n
        Some address\n
        Some address\n
        Some address\n
        Some postcode\n
        """
        recipient_address = Paragraph(address, styles["LetterBody"])

        # create a table for our header elementsj
        header_elements = [[logo, address]]
        table = Table(header_elements)
        elements.append(table)

        lipsum = [
            'Donec nec nunc eu ante luctus sodales eu ac massa. Duis id auctor sapien. Sed vel faucibus sem. Suspendisse potenti. Proin ut augue condimentum, semper leo sed, laoreet odio. Nam lobortis vel elit sit amet egestas. Vestibulum congue nisi non semper sollicitudin.',
            ]

        elements.append(Paragraph(datetime.datetime.now().strftime("%d %B %y"), styles['DateLine']))
        elements.append(Paragraph('Letter title', styles['LetterTitle']))
        elements.append(Paragraph('Dear sir or madam', styles['Salutation']))
        for i, par in enumerate(lipsum):
            elements.append(Paragraph(par, styles['LetterBody']))

        doc.build(
                elements,
                onFirstPage=self._first_page,
                onLaterPages=self._subsequent_pages,
                canvasmaker=NumberedCanvas
            )


if __name__ == '__main__':
    test = MyPrint()
    test.print_lipsum()
