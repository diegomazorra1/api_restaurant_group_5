from rest_framework import serializers

from api_restaurant_group_5.library.models import Author, Book
from api_restaurant_group_5.library.serializers.author_serializer import AuthorSerializer


class BookFromGoogleSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = ["id", "title", "authors", "description"]

    def create(self, validated_data):
        authors_data = self.initial_data.pop("authors")
        book = Book.objects.create(**validated_data)
        for author_data in authors_data:
            author, _ = Author.objects.get_or_create(name=author_data)
            book.authors.add(author)
        return book

    def update(self, instance, validated_data):
        authors_data = validated_data.pop("authors")
        instance = super().update(instance, validated_data)
        instance.authors.clear()
        for author_data in authors_data:
            author, _ = Author.objects.get_or_create(name=author_data["name"])
            instance.authors.add(author)
        return instance
