# -*- coding: utf-8 -*-
from django.forms import widgets
from rest_framework.serializers import HyperlinkedModelSerializer
from letters.models import (
    ContentTemplate,
    LetterFile,
    Letterhead,
    LetterText,
    LetterVariable,
    Logo
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


class LetterFileSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = LetterFile
        fields = ('url', 'letterfile')


class LetterheadSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Letterhead
        fields = (
            'url',
            'name',
            'logo',
            'layout',
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


class LetterVariableSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = LetterVariable
        fields = ('url', 'letter_variable',)


class LogoSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Logo
        fields = ('url', 'image')
