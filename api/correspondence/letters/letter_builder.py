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
from .letter_design import STYLES
from .letter_processor import ProcessedText
from .models import Letterhead, ContentTemplate, LetterText


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
    def __init__(self, letterhead, content_template, letter_text, response_FLO):
        """Constructor"""
        self.letterhead = letterhead
        self.content_template = content_template
        self.letter_text = letter_text
        self.response_FLO = response_FLO
        self.pagesize = A4
        self.width, self.height = self.pagesize

    def run(self):
        """
        Run the report
        """
        self.doc = SimpleDocTemplate(
                self.response_FLO,
                rightMargin=15*mm,
                leftMargin=15*mm,
                topMargin=20*mm,
                bottomMargin=30*mm,
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

        # Recipient address block
        ptext = "<font size=12>" + "<br/>".join(
                [
                    self.letter_text.addressee,
                    self.letter_text.address_1, 
                    self.letter_text.address_2, 
                    self.letter_text.address_3, 
                    self.letter_text.town, 
                    self.letter_text.postcode, 
                    "</font>",
                ]
            )
        p = Paragraph(ptext, STYLES['Normal'])
        p.wrapOn(canvas, doc.width-300, doc.height)
        p.drawOn(canvas, 15*mm, 197*mm)

        # Footer
        footer = Paragraph(self.letter_text.barcode, STYLES['Normal'])
        w, h = footer.wrap(doc.width, doc.bottomMargin)
        footer.drawOn(canvas, doc.leftMargin, h)

        # Release the canvas
        canvas.restoreState()

    def subsequent_pages(self, canvas, doc):
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
        footer = Paragraph(self.letter_text.barcode, STYLES['Normal'])
        w, h = footer.wrap(doc.width, doc.bottomMargin)
        footer.drawOn(canvas, doc.leftMargin, h)

        # Release the canvas
        canvas.restoreState()

    def insert_content(self):
        """
        Inserts the flowable elements into our letter.
        """
        # Draw things on the PDF. Here's where the PDF generation happens.
        # See the ReportLab documentation for full list of functionality.
        self.elements.append(Paragraph(self.letter_text.date_sent.strftime("%d %B %Y"), STYLES['DateLine']))
        self.elements.append(Paragraph(self.letter_text.letter_title, STYLES['LetterTitle']))
        if self.letter_text.addressee_is_organisation:
            salutation = "Dear sir or madam,"
            sign_off = "Yours faithfully,"
        else:
            salutation = "Dear " + self.letter_text.addressee + ","
            sign_off = "Yours sincerely,"
        self.elements.append(Paragraph(salutation, STYLES['Salutation']))
        flowable_text = ProcessedText(
                self.content_template,
                self.letter_text
            ).process().decode('utf-8')
        for i, par in enumerate(flowable_text.split('\n')):
            self.elements.append(Paragraph(par, STYLES['LetterBody']))
        self.elements.append(Paragraph(sign_off, STYLES['Salutation']))
        self.elements.append(Paragraph(self.letter_text.sender_name, STYLES['Signature']))
        self.elements.append(Paragraph(self.letter_text.sender_title, STYLES['SignatoryTitle']))
