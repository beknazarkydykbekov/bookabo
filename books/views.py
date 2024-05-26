from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.mixins import CreateModelMixin
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema
from rest_framework.viewsets import GenericViewSet

from .filters import BookFilter
from .models import Book, UserFavourite, Feedback
from .serializers import BookDetailSerializer, BookSerializer, UserFavouriteSerializer, FeedbackSerializer


class BookPagination(PageNumberPagination):
    page_size = 15
    page_size_query_param = 'page_size'
    max_page_size = 100


class BookListAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = BookFilter
    pagination_class = BookPagination


class BookRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = BookDetailSerializer


class AddToFavouritesAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        request={
            'application/json': {
                'type': 'object',
                'properties': {
                    'book_id': {
                        'type': 'integer',
                        'example': 1,
                    },
                },
                'required': ['book_id'],
            },
        },
        responses={
            201: UserFavouriteSerializer
        },
        description="Add a book to the user's favourites.",
    )
    def post(self, *args, **kwargs):
        user = self.request.user
        book_id = self.request.data.get('book_id')
        if user and book_id:
            book = Book.objects.filter(id=book_id).first()
            favourite = UserFavourite.objects.filter(book__id=book_id, user=user).first()
            if favourite:
                return Response({'detail': 'Already registered as favourite'}, status=200)
            if book:
                new_favourite = UserFavourite.objects.create(
                    user=user,
                    book=book
                )
                serializer = UserFavouriteSerializer(new_favourite).data
                return Response(serializer, status=201)
            return Response({'detail': 'No Book object found with the given id'}, status=404)
        return Response({'detail': 'book_id is required'}, status=400)


class CreateFeedbackViewSet(GenericViewSet, CreateModelMixin):
    queryset = Feedback.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = FeedbackSerializer

    @extend_schema(
        request=FeedbackSerializer,
        responses={201: FeedbackSerializer},
        description="Create a feedback with a rating between 1 and 5."
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


