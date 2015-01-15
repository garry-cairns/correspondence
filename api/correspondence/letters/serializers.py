# -*- coding: utf-8 -*-
from django.forms import widgets
from rest_framework.serializers import HyperlinkedModelSerializer
from letters.models import (
    ContentTemplate,
    LetterText,
    LetterFile,
    LetterVariable
)
 
 
class ContentTemplateSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = ContentTemplate
        fields = (
            'url',
            'letterhead',
            'text',
            'created',
            'start_time',
            'end_time'
        )
 
 
class LetterTextSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = LetterText
        fields =  (
            'url',
            'content_template',
            'text',
            'date_sent',
            'addressee',
            'address_1',
            'address_2',
            'address_3',
            'address_4',
            'postcode',
            'our_reference',
            'your_reference',
            'barcode',
        )
 
 
class LetterFileSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = LetterFile
        fields = ('url', 'letterfile')
 
 
class LetterVariableSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = LetterVariable
        fields = ('letter_variable',)
