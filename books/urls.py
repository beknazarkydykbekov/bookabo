from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import BookListAPIView, BookRetrieveAPIView, AddToFavouritesAPIView, CreateFeedbackViewSet

router = SimpleRouter()

router.register('feedback/leave', CreateFeedbackViewSet, basename='create-feedback')

urlpatterns = [
    path('books/', BookListAPIView.as_view(), name='book-list'),
    path('book/<int:pk>/', BookRetrieveAPIView.as_view(), name='book-retrieve'),
    path('book/add-to-fav/', AddToFavouritesAPIView.as_view(), name='book-add-to-favourite'),
] + router.urls
