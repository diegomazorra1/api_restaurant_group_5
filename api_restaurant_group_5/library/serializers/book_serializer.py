from rest_framework.serializers import ModelSerializer

from api_restaurant_group_5.library.models import Book


class BookSerializer(ModelSerializer):
    """Serializer for Orders."""

    class Meta:
        model = Book
        fields = ("id", "title", "subtitle", "authors", "categories", "description", "publish_time", "editor", "image")

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["authors"] = (
            [author.name for author in instance.authors.all()] if "authors" in representation else None
        )
        representation["categories"] = (
            [category.name for category in instance.categories.all()] if "categories" in representation else None
        )
        representation["editor"] = instance.editor.name if instance.editor else None
        return representation
