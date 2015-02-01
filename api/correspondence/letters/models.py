# -*- coding: utf-8 -*-
from django.core.cache import cache
from django.db.models import (
    CharField,
    DateTimeField,
    FileField,
    ForeignKey,
    ImageField,
    IntegerField,
    Model,
    TextField,
)


class ContentTemplate(Model):
    """ContentTemplate object. Attributes:
    * :attr: `~letters.models.ContentTemplate.letterhead` - link to current
      letterhead
    * :attr: `~letters.models.ContentTemplate.name` - document name
      letterhead
    * :attr: `~letters.models.ContentTemplate.text` - string representing
      the letter's full text
    * :attr: `~letters.models.ContentTemplate.created` - date on which the
      content template was created
    * :attr: `~letters.models.ContentTemplate.start_time` - date on which
      the content template was made available to users
    * :attr: `~letters.models.ContentTemplate.end_time` - date on which the
      content template ceased being available to users
    """
    letterhead = ForeignKey("Letterhead")
    text = TextField()
    created = DateTimeField()
    start_time = DateTimeField()
    end_time = DateTimeField()


class LetterFile(Model):
    """LetterFile object. Attributes:
    * :attr: `~letters.models.LetterFile.letterfile` - PDF generated by
      the service
    """
    letterfile = FileField()


class Letterhead(Model):
    """Letterhead object. Attributes:
    * :attr: `~letters.models.Letterhead.name` - letterhead name
    * :attr: `~letters.models.Letterhead.font` - letterhead main font
    * :attr: `~letters.models.Letterhead.logo` - link to letterhead logo
    * :attr: `~letters.models.Letterhead.logo_x` - logo x co-ordinate
    * :attr: `~letters.models.Letterhead.logo_y` - logo y co-ordinate
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
    logo = ForeignKey("Logo")
    logo_x = IntegerField(help_text="Distance in mm from left edge of page to left edge of logo")
    logo_y = IntegerField(help_text="Distance in mm from top edge of page to top edge of logo")
    return_contacts = TextField()
    return_contacts_x = IntegerField(help_text="Distance in mm from left edge of page to left edge of return contacts")
    return_contacts_y = IntegerField(help_text="Distance in mm from top edge of page to top edge of return contacts")
    # Reference blocks handle position only, values provided with LetterText to minimize object creation events
    your_reference_x = IntegerField(help_text="Distance in mm from left edge of page to left edge of recipient's reference")
    your_reference_y = IntegerField(help_text="Distance in mm from top edge of page to top edge of recipient's reference")
    our_reference_x = IntegerField(help_text="Distance in mm from left edge of page to left edge of our reference")
    our_reference_y = IntegerField(help_text="Distance in mm from top edge of page to top edge of our reference")
    created = DateTimeField()
    start_time = DateTimeField()
    end_time = DateTimeField()


class LetterText(Model):
    """LetterText object. Attributes:
    * :attr: `~letters.models.LetterText.content_template` - link to
      relevant content template
      the letter's full text
    * :attr: `~letters.models.LetterText.text` - string representing
      the letter's full text
    * :attr: `~letters.models.LetterText.date_sent` - date on which we
      issued the letter
    * :attr: `~letters.models.LetterText.addressee` - person or
      organisation to whom the letter was addressed
    * :attr: `~letters.models.LetterText.address_1` - first line address
    * :attr: `~letters.models.LetterText.address_2` - second line address
    * :attr: `~letters.models.LetterText.address_3` - third line address
    * :attr: `~letters.models.LetterText.address_4` - fourth line address
    * :attr: `~letters.models.LetterText.postcode` - postcode
    * :attr: `~letters.models.LetterText.our_reference` - our reference
      number, if applicable
    * :attr: `~letters.models.LetterText.your_reference` - the addressee's
      reference number, if applicable
    * :attr: `~letters.models.LetterText.barcode` - the barcode string
      from which we will generate the QR code
    * :attr: `~letters.models.LetterText.additional_data` - client-provided
      string of JSON with additional variables
    """
    content_template = ForeignKey("ContentTemplate")
    text = TextField()
    date_sent = DateTimeField()
    addressee = CharField(max_length=100)
    address_1 = CharField(max_length=100)
    address_2 = CharField(max_length=100)
    address_3 = CharField(max_length=100)
    address_4 = CharField(max_length=100)
    postcode = CharField(max_length=100)
    our_reference = CharField(max_length=100)
    your_reference = CharField(max_length=100)
    barcode = CharField(max_length=100)
    additional_data = TextField() # client packages these into one string


class LetterVariable(Model):
    """LetterVariable object. Attributes:
    * :attr: `~letters.models.LetterVariable.letter_variable` - variable
      available in a given template
    """
    letter_variable = CharField(max_length=100)


class Logo(Model):
    """Logo object. Attributes:
    * :attr: `~letters.models.Logo.image` - logo image
    """
    image = ImageField()
