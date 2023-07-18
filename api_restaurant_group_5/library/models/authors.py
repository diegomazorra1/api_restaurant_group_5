from django.db import models
from django.db.models import CharField


class Author(models.Model):
    """This is the author model"""

    name = CharField(max_length=256)
