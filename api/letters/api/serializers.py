from django.contrib.auth.models import User, Group
from rest_framework import serializers


class TemplateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Template
        fields = ('url', 'letterhead', 'template')


class LetterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Letter
        fields = ('url', 'template', 'content')
