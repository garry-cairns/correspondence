# -*- coding: utf-8 -*-
from rest_framework.renderers import BaseRenderer


class PDFRenderer(BaseRenderer):
    """
    Custom renderer to return content as a PDF.
    """
    media_type = "application/pdf"
    format = "pdf"
    charset = None
    render_style = "binary"

    def render(self, data, media_type=None, renderer_context=None):
        return data