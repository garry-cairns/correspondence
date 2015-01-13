from django.db import models


class Letterhead(models.Model):
    logo = models.ImageField()
    contact_information = models.TextField()


class Template(models.Model):
    letterhead = models.ForeignKey('letterhead')
    content = models.TextField()


class Letter(models.Model):
    template = models.ForeignKey('template')
    variables = models.TextField()
