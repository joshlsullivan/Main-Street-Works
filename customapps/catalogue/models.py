from django.db import models

from oscar.apps.catalogue.abstract_models import AbstractProduct

from location.models import Location


class Product(AbstractProduct):
    location = models.IntegerField(blank=True)


from oscar.apps.catalogue.models import *