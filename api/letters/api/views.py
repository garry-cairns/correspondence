from rest_framework import viewsets
from .models import Letter, Template
from .serializers import LetterSerializer, TemplateSerializer


class TemplateViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows letter templates to be viewed or edited.
    """
    queryset = Template.objects.all()
    serializer_class = TemplateSerializer


class LetterViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows individual letter to be viewed or edited.
    """
    queryset = Letter.objects.all()
    serializer_class = LetterSerializer
