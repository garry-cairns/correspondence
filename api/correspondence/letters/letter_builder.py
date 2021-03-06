# -*- coding: utf-8 -*-
import datetime
import sys
from reportlab.graphics import renderPDF
from reportlab.graphics.barcode.qr import QrCodeWidget
from reportlab.graphics.shapes import Drawing
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
from .letter_design import STYLES
from .letter_processor import ProcessedText
from .models import Letterhead, ContentTemplate, Letter


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
                10 * mm,
                "Page %d of %d" % (self._pageNumber, page_count)
            )


class LetterCanvas(object):
    def __init__(self, letterhead, content_template, letter, response_FLO):
        """Constructor"""
        self.letterhead = letterhead
        self.content_template = content_template
        self.letter = letter
        self.response_FLO = response_FLO
        self.pagesize = A4
        self.width, self.height = self.pagesize

    def run(self):
        """
        Run the report
        """
        self.doc = SimpleDocTemplate(
                self.response_FLO,
                rightMargin=self.letterhead.right_margin*mm,
                leftMargin=self.letterhead.left_margin*mm,
                topMargin=self.letterhead.top_margin*mm,
                bottomMargin=self.letterhead.bottom_margin*mm,
                pagesize=self.pagesize,
            )
        self.elements = [Spacer(1, 67*mm)]
        self.insert_content()
        self.doc.build(
                self.elements,
                onFirstPage=self.first_page,
                onLaterPages=self.subsequent_pages,
                canvasmaker=NumberedCanvas
            )

    def first_page(self, canvas, doc):
        """
        Defines layout for the first page of our letter.
        """
        # Save the state of our canvas so we can draw on it
        canvas.saveState()

        # Logo block
        logo = Image(
                self.letterhead.logo.image,
                width=self.letterhead.logo_width*mm,
                height=self.letterhead.logo_height*mm
            )
        logo.wrapOn(canvas, doc.width/2.0, doc.height)
        logo.drawOn(
                canvas,
                self.letterhead.logo_x*mm,
                (297-self.letterhead.logo_y-self.letterhead.logo_height)*mm
            )

        # Return address block
        ptext = "<br/>".join([line for line in self.letterhead.return_contacts.split('\n')])
        p = Paragraph(ptext, STYLES['ReturnAddress'])
        p.wrapOn(
                canvas,
                doc.width/3.0,
                doc.height
            )
        p.drawOn(
                canvas,
                self.letterhead.return_contacts_x*mm,
                (257-self.letterhead.return_contacts_y)*mm
            )

        # Reference block
        ptext = "Your reference: " + self.letter.your_reference
        p = Paragraph(ptext, STYLES['ReturnAddress'])
        p.wrapOn(
                canvas,
                doc.width/3.0,
                doc.height
            )
        p.drawOn(
                canvas,
                self.letterhead.your_reference_x*mm,
                (257-self.letterhead.your_reference_y)*mm
            )
        ptext = "Our reference: " + self.letter.our_reference
        p = Paragraph(ptext, STYLES['ReturnAddress'])
        p.wrapOn(
                canvas,
                doc.width/3.0,
                doc.height
            )
        p.drawOn(
                canvas,
                self.letterhead.our_reference_x*mm,
                (257-self.letterhead.our_reference_y)*mm
            )

        # Recipient address block
        ptext = "<font size=12>" + "<br/>".join(
                [
                    (" ").join([
                        self.letter.addressee_title,
                        self.letter.addressee_first_name,
                        self.letter.addressee_second_name,
                    ]),
                    self.letter.address_1, 
                    self.letter.address_2, 
                    self.letter.address_3, 
                    self.letter.town, 
                    self.letter.postcode, 
                    "</font>",
                ]
            )
        p = Paragraph(ptext, STYLES['Normal'])
        p.wrapOn(canvas, doc.width-300, doc.height)
        p.drawOn(canvas, 15*mm, 197*mm)

        # Footer
        # See http://stackoverflow.com/a/13132282
        qr_code = QrCodeWidget(self.letter.barcode)
        drawing = Drawing(45, 45)
        drawing.add(qr_code)
        renderPDF.draw(drawing, canvas, 1, 1)
        footer = Paragraph(self.letter.barcode, STYLES['Normal'])
        w, h = footer.wrap(doc.width, doc.bottomMargin)
        footer.drawOn(canvas, doc.leftMargin+50, h)

        # Release the canvas
        canvas.restoreState()

    def subsequent_pages(self, canvas, doc):
        """
        Defines layout for all pages of our letter but the first.
        """
        # Save the state of our canvas so we can draw on it
        canvas.saveState()

        # Header
        header = Paragraph(self.content_template.name, STYLES['Normal'])
        w, h = header.wrap(doc.width, doc.topMargin)
        header.drawOn(canvas, doc.leftMargin, doc.height + doc.topMargin + doc.bottomMargin - h*mm)

        # Footer
        qr_code = QrCodeWidget(self.letter.barcode)
        drawing = Drawing(45, 45)
        drawing.add(qr_code)
        renderPDF.draw(drawing, canvas, 1, 1)
        footer = Paragraph(self.letter.barcode, STYLES['Normal'])
        w, h = footer.wrap(doc.width, doc.bottomMargin)
        footer.drawOn(canvas, doc.leftMargin+50, h)

        # Release the canvas
        canvas.restoreState()

    def insert_content(self):
        """
        Inserts the flowable elements into our letter.
        """
        # Draw things on the PDF. Here's where the PDF generation happens.
        # See the ReportLab documentation for full list of functionality.
        self.elements.append(Paragraph(self.letter.date_sent.strftime("%d %B %Y"), STYLES['DateLine']))
        self.elements.append(Paragraph(self.letter.letter_title, STYLES['LetterTitle']))
        if self.letter.addressee_organisation and not self.letter.addressee_title:
            salutation = "Dear sir or madam,"
            sign_off = "Yours faithfully,"
        else:
            salutation = (" ").join([
                self.letter.addressee_title,
                self.letter.addressee_second_name,
            ])
            salutation += ","
            sign_off = "Yours sincerely,"
        self.elements.append(Paragraph(salutation, STYLES['Salutation']))
        flowable_text = ProcessedText(
                self.content_template,
                self.letter
            ).process().decode('utf-8')
        for i, par in enumerate(flowable_text.split('\n')):
            self.elements.append(Paragraph(par, STYLES['LetterBody']))
        self.elements.append(Paragraph(sign_off, STYLES['Salutation']))
        self.elements.append(Paragraph(self.letter.sender_name, STYLES['Signature']))
        self.elements.append(Paragraph(self.letter.sender_title, STYLES['SignatoryTitle']))
