from django.db import models
from django.db.models import CharField


class Category(models.Model):
    """This is the category model"""

    name = CharField(max_length=256)
