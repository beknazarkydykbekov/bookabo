from books.models import Book, UserFavourite
from users.models import CustomUser


def get_avg_rating(rate_count: int, rate_sum: int) -> float:
    if rate_sum == 0 == rate_count:
        return 0
    return rate_sum / rate_count


def is_favourite_book(book: Book, user: CustomUser):
    return True if UserFavourite.objects.filter(book=book, user=user).first() else False
