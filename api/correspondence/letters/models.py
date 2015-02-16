# -*- coding: utf-8 -*-
import datetime
from django.core.cache import cache
from django.db.models import (
    BooleanField,
    CharField,
    DateTimeField,
    FileField,
    ForeignKey,
    ImageField,
    IntegerField,
    ManyToManyField,
    Model,
    TextField,
)
from django.http import HttpResponse


class ContentTemplate(Model):
    """ContentTemplate object. Attributes:
    * :attr: `~letters.models.ContentTemplate.template_name` - document name
    * :attr: `~letters.models.ContentTemplate.text` - string representing
      the letter's full text and the variables it expects. Django template.
    * :attr: `~letters.models.ContentTemplate.created` - date on which the
      content template was created
    * :attr: `~letters.models.ContentTemplate.start_time` - date on which
      the content template was made available to users
    * :attr: `~letters.models.ContentTemplate.end_time` - date on which the
      content template ceased being available to users
    """
    name = CharField(max_length=100)
    text = TextField()
    created = DateTimeField(auto_now_add=True)
    start_time = DateTimeField(
            blank=True,
            null=True
        )
    end_time = DateTimeField(
            blank=True,
            null=True
        )

    def __str__(self):
        return self.name + ' ' + self.start_time.strftime("%d %B %Y")


class Letterhead(Model):
    """Letterhead object. Attributes:
    * :attr: `~letters.models.Letterhead.name` - letterhead name
    * :attr: `~letters.models.Letterhead.font` - letterhead main font
    * :attr: `~letters.models.Letterhead.left_margin` - left margin mm
    * :attr: `~letters.models.Letterhead.top_margin` - top margin mm
    * :attr: `~letters.models.Letterhead.right_margin` - right margin mm
    * :attr: `~letters.models.Letterhead.bottom_margin` - bottom margin mm
    * :attr: `~letters.models.Letterhead.logo` - link to letterhead logo
    * :attr: `~letters.models.Letterhead.logo_x` - logo x co-ordinate
    * :attr: `~letters.models.Letterhead.logo_y` - logo y co-ordinate
    * :attr: `~letters.models.Letterhead.logo_width` - logo width
    * :attr: `~letters.models.Letterhead.logo_height` - logo height
    * :attr: `~letters.models.Letterhead.return_contacts` - return contact information
    * :attr: `~letters.models.Letterhead.return_contacts_x` - return contact information x co-ordinate
    * :attr: `~letters.models.Letterhead.return_contacts_y` - return contact information y co-ordinate
    * :attr: `~letters.models.Letterhead.your_reference_x` - recipient reference x co-ordinate
    * :attr: `~letters.models.Letterhead.your_reference_y` - recipient reference x co-ordinate
    * :attr: `~letters.models.Letterhead.our_reference_x` - our reference x co-ordinate
    * :attr: `~letters.models.Letterhead.our_reference_y` - our reference y co-ordinate
    * :attr: `~letters.models.Letterhead.created` - date on which the
      letterhead was created
    * :attr: `~letters.models.Letterhead.start_time` - date on which the
      letterhead was made available to users
    * :attr: `~letters.models.Letterhead.end_time` - date on which the
      letterhead ceased being available to users
    """
    COURIER = 1
    HELVETICA = 2
    TIMES = 3
    FONT_CHOICES = (
            (COURIER, 'Courier'),
            (HELVETICA, 'Helvetica'),
            (TIMES, 'Times'),
        )
    name = CharField(max_length=100)
    font = IntegerField(
            choices=FONT_CHOICES,
            default=HELVETICA,
            help_text="Choices are restricted to those available as standard in PDFs. This is essential to our archiving requirements.",
        )
    left_margin = IntegerField(help_text="Distance in mm from left edge of page to left edge of body text")
    top_margin = IntegerField(help_text="Distance in mm from top edge of page to top edge of body text")
    right_margin = IntegerField(help_text="Distance in mm from right edge of page to right edge of body text")
    bottom_margin = IntegerField(help_text="Distance in mm from bottom edge of page to bottom edge of body text")
    logo = ForeignKey("Logo")
    logo_x = IntegerField(help_text="Distance in mm from left edge of page to left edge of logo")
    logo_y = IntegerField(help_text="Distance in mm from top edge of page to top edge of logo")
    logo_width = IntegerField(help_text="Logo width in mm")
    logo_height = IntegerField(help_text="Logo height in mm")
    return_contacts = TextField()
    return_contacts_x = IntegerField(help_text="Distance in mm from left edge of page to left edge of return contacts")
    return_contacts_y = IntegerField(help_text="Distance in mm from top edge of page to top edge of return contacts")
    # Reference blocks handle position only, values provided with Letter to minimize object creation events
    your_reference_x = IntegerField(help_text="Distance in mm from left edge of page to left edge of recipient's reference")
    your_reference_y = IntegerField(help_text="Distance in mm from top edge of page to top edge of recipient's reference")
    our_reference_x = IntegerField(help_text="Distance in mm from left edge of page to left edge of our reference")
    our_reference_y = IntegerField(help_text="Distance in mm from top edge of page to top edge of our reference")
    created = DateTimeField(auto_now_add=True)
    start_time = DateTimeField(
            blank=True,
            null=True
        )
    end_time = DateTimeField(
            blank=True,
            null=True
        )

    def __str__(self):
        return self.name + ' ' + self.start_time.strftime("%d %B %Y")


class Letter(Model):
    """Letter object. Attributes:
    * :attr: `~letters.models.Letter.letterhead` - link to current
      letterhead
    * :attr: `~letters.models.Letter.content_template` - link to
      relevant content template
    * :attr: `~letters.models.Letter.date_sent` - date on which we
      issued the letter
    * :attr: `~letters.models.Letter.addressee_title` - title of the person
      to whom the letter was addressed, blank if addressee is organisation
    * :attr: `~letters.models.Letter.addressee_first_name` - first name of 
      the person to whom letter addressed, blank if addressee is org
    * :attr: `~letters.models.Letter.addressee_second_name` - second name 
      of the person to whom letter addressed, blank if addressee is org
    * :attr: `~letters.models.Letter.addressee_organisation` - name 
      of the organisation to whom letter addressed, blank if none
    * :attr: `~letters.models.Letter.address_1` - first line address
    * :attr: `~letters.models.Letter.address_2` - second line address
    * :attr: `~letters.models.Letter.address_3` - third line address
    * :attr: `~letters.models.Letter.address_4` - fourth line address
    * :attr: `~letters.models.Letter.postcode` - postcode
    * :attr: `~letters.models.Letter.our_reference` - our reference
      number, if applicable
    * :attr: `~letters.models.Letter.your_reference` - the addressee's
      reference number, if applicable
    * :attr: `~letters.models.Letter.barcode` - the barcode string
      from which we will generate the QR code
    * :attr: `~letters.models.Letter.additional_data` - client-provided
      dictionary with additional variables and their values
    """
    DR = 1
    MISS = 2
    MR = 3
    MRS = 4
    MS = 5
    TITLE_CHOICES = (
            (DR, 'Dr'),
            (MISS, 'Miss'),
            (MR, 'Mr'),
            (MRS, 'Mrs'),
            (MS, 'Ms'),
        )
    letterhead = ForeignKey("Letterhead")
    content_template = ForeignKey("ContentTemplate")
    addressee_title = CharField(
            max_length=100,
            blank=True,
            null=True,
        )
    addressee_first_name = CharField(
            max_length=100,
            blank=True,
            null=True,
        )
    addressee_second_name = CharField(
            max_length=100,
            blank=True,
            null=True,
        )
    addressee_organisation = CharField(
            max_length=100,
            blank=True,
            null=True,
        )
    address_1 = CharField(max_length=100)
    address_2 = CharField(
            max_length=100,
            blank=True,
            null=True,
        )
    address_3 = CharField(
            max_length=100,
            blank=True,
            null=True,
        )
    town = CharField(max_length=100)
    postcode = CharField(max_length=100)
    our_reference = CharField(
            max_length=100,
            blank=True,
            null=True,
        )
    your_reference = CharField(
            max_length=100,
            blank=True,
            null=True,
        )
    date_sent = DateTimeField(auto_now_add=True)
    letter_title = CharField(max_length=100)
    addressee_is_representative = BooleanField(default=False)
    sender_name = CharField(max_length=100)
    sender_title = CharField(max_length=100)
    barcode = CharField(max_length=100)
    additional_data = TextField( # client packages these into one string
            blank=True,
            null=True,
        )

    def compulsory_variable_dictionary(self):
        """
        Bundles those attributes needed for every letter into a
        dictionary for processing by the letter_processor.
        """
        return {
                'addressee_title': self.addressee_title,
                'addressee_first_name': self.addressee_first_name,
                'addressee_second_name': self.addressee_second_name,
                'addressee_organisation': self.addressee_organisation,
                'address_1': self.address_1,
                'address_2': self.address_2,
                'address_3': self.address_3,
                'town': self.town,
                'postcode': self.postcode,
                'our_reference': self.our_reference,
                'your_reference': self.your_reference,
                'addressee_is_representative': self.addressee_is_representative,
                'sender_name': self.sender_name,
                'sender_title': self.sender_title,
                }

    def __str__(self):
        return self.barcode


class LetterVariable(Model):
    """LetterVariable object. Attributes:
    * :attr: `~letters.models.LetterVariable.content_template` - templates
      to which a variable is attached
    * :attr: `~letters.models.LetterVariable.variable_name` - variable
      available in a given template
    """
    content_template = ManyToManyField("ContentTemplate")
    variable_name = CharField(max_length=100)

    def __str__(self):
        return self.variable_name


class Logo(Model):
    """Logo object. Attributes:
    * :attr: `~letters.models.Logo.name` - logo name
    * :attr: `~letters.models.Logo.image` - logo image
    * :attr: `~letters.models.Logo.created` - date on which the
      logo was created
    * :attr: `~letters.models.Logo.start_time` - date on which the
      logo was made available to users
    * :attr: `~letters.models.Logo.end_time` - date on which the
      logo ceased being available to users
    """
    name = CharField(max_length=100)
    image = ImageField()
    created = DateTimeField(auto_now_add=True)
    start_time = DateTimeField(
            blank=True,
            null=True
        )
    end_time = DateTimeField(
            blank=True,
            null=True
        )

    def __str__(self):
        return self.name + ' ' + self.start_time.strftime("%d %B %Y")
