from django.db import models
from django.db.models import PROTECT, CharField, ForeignKey, ImageField, ManyToManyField, TextField, TimeField


class Book(models.Model):
    """This is the book model"""

    title = CharField(max_length=256)
    subtitle = CharField(max_length=256)
    authors = ManyToManyField("library.Author", related_name="authors", blank=True)
    categories = ManyToManyField("library.Category", related_name="categories", blank=True)
    description = TextField(blank=True, null=True)
    publish_time = TimeField(null=True, blank=True)
    editor = ForeignKey("library.Editor", on_delete=PROTECT, null=True)
    image = ImageField("library.Editor", blank=True, null=True)
