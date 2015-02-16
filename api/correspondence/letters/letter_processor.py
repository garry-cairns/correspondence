# -*- coding: utf-8 -*-
import ast
from django.template import Template
from django.template.response import SimpleTemplateResponse
from .models import ContentTemplate, Letter


class ProcessedText(object):
    def __init__(self, content_template, letter_text):
        """Constructor"""
        self.content_template = content_template
        self.letter_text = letter_text
        self.variables = self.content_template.lettervariable_set.all()
        try:
            self.variable_values = ast.literal_eval(
                    letter_text.additional_data
                )
        except:
            self.variable_values = {}

    def process(self):
        """
        Get the relevant variables for the content template. Process the
        letter_text provided through your templating language using those
        variables and return the final text.
        """
        #additional_variable_dictionary = {
        #        v.variable_name: v.variable_value for v in self.variables
        #    }
        process_dictionary = dict(
                self.letter_text.compulsory_variable_dictionary(),
                **self.variable_values
            )
        template = Template(self.content_template.text)
        return SimpleTemplateResponse(
                template,
                process_dictionary
            ).render().content
