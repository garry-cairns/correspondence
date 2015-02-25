# -*- coding: utf-8 -*-
from django.http import HttpResponse
from rest_framework import renderers
from rest_framework.decorators import api_view, detail_route
from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer
from rest_framework_ember.renderers import JSONRenderer as EmberJSONRenderer
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.viewsets import ModelViewSet
from letters.letter_builder import LetterCanvas
from letters.models import (
    ContentTemplate,
    Letterhead,
    Letter,
    LetterVariable,
    Logo
)
from letters.renderers import PDFRenderer
from letters.serializers import (
    ContentTemplateSerializer,
    LetterheadSerializer,
    LetterSerializer,
    LetterVariableSerializer,
    LogoSerializer
)


@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'content_template': reverse('content-template-list', request=request, format=format)
})


class ContentTemplateViewSet(ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = ContentTemplate.objects.all()
    serializer_class = ContentTemplateSerializer


class LetterheadViewSet(ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Letterhead.objects.all()
    serializer_class = LetterheadSerializer


class LetterViewSet(ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    Append 'letter' to the URL to retrieve the instance as a formatted
    PDF letter.
    """
    queryset = Letter.objects.all()
    serializer_class = LetterSerializer
    renderer_classes = [EmberJSONRenderer, BrowsableAPIRenderer, PDFRenderer]

    @detail_route(renderer_classes=[PDFRenderer])
    def letter(self, request, *args, **kwargs):
        """
        Takes a Letter instance and a django request and returns
        a PDF letter as the request response.
        """
        letter = self.get_object()
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


class LetterVariableViewSet(ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = LetterVariable.objects.all()
    serializer_class = LetterVariableSerializer


class LogoViewSet(ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Logo.objects.all()
    serializer_class = LogoSerializer
