from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter, extend_schema, extend_schema_view
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from api_restaurant_group_5.library.serializers import BookFromGoogleSerializer, BookSerializer
from api_restaurant_group_5.utils.fetch_book_details import fetch_book_details


@extend_schema_view(
    post=extend_schema(
        parameters=[
            OpenApiParameter("book_id", OpenApiTypes.STR, required=True),
        ],
        responses={
            200: BookFromGoogleSerializer,
        },
    )
)
class BookCreateFromGoogleAPI(APIView):
    permission_classes = [AllowAny]
    """This view will create a new book from api google id"""

    def post(self, request, **kwargs):
        book_id = request.query_params.get("book_id", "")
        if not book_id:
            return Response({"error": "No book ID provided"}, status=status.HTTP_400_BAD_REQUEST)

        book_details = fetch_book_details(book_id)
        if not book_details:
            return Response({"error": "Failed to fetch book details"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        serializer = BookFromGoogleSerializer(
            data={
                "title": book_details["volumeInfo"].get("title", ""),
                "authors": book_details["volumeInfo"].get("authors", []),
                "description": book_details["volumeInfo"].get("description", ""),
            }
        )

        if serializer.is_valid():
            book = serializer.save()
            return Response(BookSerializer(book).data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
