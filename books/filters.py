import django_filters
from .models import Book


class BookFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    genre = django_filters.NumberFilter(field_name='genre__id')
    author = django_filters.NumberFilter(field_name='author__id')
    publication_date = django_filters.DateFromToRangeFilter()

    class Meta:
        model = Book
        fields = ['title', 'publication_date', 'genre', 'author']
