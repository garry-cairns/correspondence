# -*- coding: utf-8 -*-
from django.http import HttpResponse
from rest_framework.renderers import BaseRenderer
from letters.letter_builder import LetterCanvas
from letters.models import Letter


class PDFRenderer(BaseRenderer):
    """
    Custom renderer to return content as a PDF.
    """
    media_type = "application/pdf"
    format = "pdf"
    charset = None
    render_style = "binary"

    def render(self, data, media_type=None, renderer_context=None):
        """
        Takes a Letter instance and a django request and returns
        a PDF letter as the request response.
        """
        letter = Letter.objects.get(barcode=data['barcode'])
        response = HttpResponse(content_type="application/pdf")
        response["Content-Disposition"] = "attachment; filename={0}.pdf".format(letter.letter_title)
        letter = LetterCanvas(
                letter.letterhead,
                letter.content_template,
                letter,
                response,
            )
        letter.run()
        return response