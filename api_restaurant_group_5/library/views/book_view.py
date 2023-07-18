import requests
from django.db.models import Q
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter, extend_schema, extend_schema_view
from rest_framework import mixins, status, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from api_restaurant_group_5.library.models import Book
from api_restaurant_group_5.library.serializers import BookSerializer


@extend_schema_view(
    list=extend_schema(
        parameters=[
            OpenApiParameter("query", OpenApiTypes.STR, required=False),
        ]
    )
)
class BookSearchAPI(
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
    mixins.DestroyModelMixin,
    mixins.CreateModelMixin,
):
    permission_classes = [AllowAny]
    serializer_class = BookSerializer
    queryset = Book.objects.all()

    def list(self, request, *args, **kwargs):
        query = request.query_params.get("query", "")

        if query:
            books = Book.objects.filter(
                Q(title__icontains=query)
                | Q(subtitle__icontains=query)
                | Q(authors__name__icontains=query)
                | Q(description__icontains=query)
                | Q(publish_time__icontains=query)
                | Q(editor__name__icontains=query)
            )
            serialized_books = BookSerializer(books, many=True)
            if books:
                return Response(serialized_books.data, status=status.HTTP_200_OK)
            google_books_api = "https://www.googleapis.com/books/v1/volumes"
            params = {"q": f"{query}"}
            response = requests.get(google_books_api, params=params)
            if response.status_code == 200:
                data = response.json()
                return Response(data, status=status.HTTP_200_OK)
            return Response(status=status.HTTP_503_SERVICE_UNAVAILABLE)

        return super().list(request, *args, **kwargs)
