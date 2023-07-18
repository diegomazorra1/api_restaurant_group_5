from rest_framework import serializers

from api_restaurant_group_5.library.models import Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["name"]
