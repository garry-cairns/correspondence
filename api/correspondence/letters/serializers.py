# -*- coding: utf-8 -*-
from django.forms import widgets
from rest_framework.serializers import HyperlinkedModelSerializer
from letters.models import (
    ContentTemplate,
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
                'name',
                'text',
                'created',
                'start_time',
                'end_time'
            )


class LetterheadSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Letterhead
        fields = (
                'url',
                'name',
                'font',
                'logo',
                'logo_x',
                'logo_y',
                'logo_width',
                'logo_height',
                'return_contacts',
                'return_contacts_x',
                'return_contacts_y',
                'your_reference_x',
                'your_reference_y',
                'our_reference_x',
                'our_reference_y',
                'created',
                'start_time',
                'end_time'
            )


class LetterTextSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = LetterText
        fields =  (
                'url',
                'letterhead',
                'content_template',
                'addressee',
                'address_1',
                'address_2',
                'address_3',
                'town',
                'postcode',
                'our_reference',
                'your_reference',
                'date_sent',
                'letter_title',
                'addressee_is_organisation',
                'addressee_is_representative',
                'sender_name',
                'sender_title',
                'barcode',
                'additional_data',
            )


class LetterVariableSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = LetterVariable
        fields = (
                'url',
                'content_template',
                'variable_name',
                'variable_value',
            )


class LogoSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Logo
        fields = (
                'url',
                'name',
                'image',
                'created',
                'start_time',
                'end_time'
            )
