# -*- coding: utf-8 -*-
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.viewsets import ModelViewSet
from letters.letter_builer import LetterCanvas
from letters.models import (
    ContentTemplate,
    LetterFile,
    Letterhead,
    LetterText,
    LetterVariable,
    Logo
)
from letters.serializers import (
    ContentTemplateSerializer,
    LetterFileSerializer,
    LetterheadSerializer,
    LetterTextSerializer,
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


class LetterFileViewSet(ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = LetterFile.objects.all()
    serializer_class = LetterFileSerializer


class LetterheadViewSet(ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Letterhead.objects.all()
    serializer_class = LetterheadSerializer


class LetterTextViewSet(ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = LetterText.objects.all()
    serializer_class = LetterTextSerializer


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
