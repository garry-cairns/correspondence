# -*- coding: utf-8 -*-
from django.template import Template
from django.template.response import SimpleTemplateResponse
from .models import ContentTemplate, LetterText


class ProcessedText(object):
    def __init__(self, content_template, letter_text):
        """Constructor"""
        self.content_template = content_template
        self.letter_text = letter_text
        self.variables = self.content_template.lettervariable_set.all()
        self.variable_values = self.letter_text.additional_data

    def process(self):
        """
        Get the relevant variables for the content template. Process the
        letter_text provided through your templating language using those
        variables and return the final text.
        """
        additional_variable_dictionary = {
                v.variable_name: v.variable_value for v in self.variables
            }
        process_dictionary = dict(
                self.letter_text.compulsory_variable_dictionary(),
                **additional_variable_dictionary
            )
        template = Template(self.content_template.text)
        return SimpleTemplateResponse(
                template,
                process_dictionary
            ).render().content
