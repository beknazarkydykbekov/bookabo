from django.db import models

from users.models import CustomUser


class Genre(models.Model):
    title = models.CharField(max_length=150)

    def __str__(self):
        return self.title


class Author(models.Model):
    full_name = models.CharField(max_length=150)
    biography = models.TextField()

    def __str__(self):
        return self.full_name


class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='books')
    publication_date = models.DateField()

    def __str__(self):
        return f'{self.title} ({self.author.full_name})'

    class Meta:
        ordering = ('-publication_date',)


class Feedback(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='feedbacks')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='feedbacks')
    stars = models.PositiveIntegerField(default=0, )
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.email}"s feedback'


class UserFavourite(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user_favourites')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='favourites')
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.email}"s favourite book {self.book.title}'

