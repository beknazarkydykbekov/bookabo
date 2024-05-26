from rest_framework import serializers

from .models import Author, Book, Genre, Feedback, UserFavourite
from .utils import get_avg_rating, is_favourite_book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'genre', 'author')

    def to_representation(self, instance):
        user = self.context['request'].user
        rep = super().to_representation(instance)
        rep['genre_name'] = instance.genre.title
        rep['author_name'] = instance.author.full_name
        rep['avg_rating'] = get_avg_rating(rate_sum=sum(instance.feedbacks.filter().values_list('stars', flat=True)),
                                           rate_count=instance.feedbacks.all().count())
        rep['is_favourite'] = is_favourite_book(instance, user)
        return rep


class FeedbackListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ('id', 'comment', 'stars', 'created_at')

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['author_email'] = instance.user.email
        rep['author_name'] = instance.user.first_name
        return rep


class BookDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['genre_name'] = instance.genre.title
        rep['author_name'] = instance.author.full_name
        rep['avg_rating'] = get_avg_rating(rate_sum=sum(instance.feedbacks.filter().values_list('stars', flat=True)),
                                           rate_count=instance.feedbacks.all().count())
        rep['feedbacks'] = FeedbackListingSerializer(instance.feedbacks.all(), many=True).data
        return rep


class UserFavouriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFavourite
        fields = '__all__'


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        exclude = ('user',)
        extra_kwargs = {
            'stars': {'min_value': 1, 'max_value': 5},
        }
    
    def create(self, validated_data):
        user = self.context.get('request').user
        return Feedback.objects.create(**validated_data, user=user)
        