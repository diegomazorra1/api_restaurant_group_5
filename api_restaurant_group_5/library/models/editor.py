from django.db import models
from django.db.models import CharField


class Editor(models.Model):
    """This is the editor model"""

    name = CharField(max_length=256)
