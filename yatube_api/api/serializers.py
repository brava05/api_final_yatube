# TODO
# При указании параметров limit и offset выдача должна работать с пагинацией.
# GET Возвращает все подписки пользователя,
# сделавшего запрос. Анонимные запросы запрещены.

from rest_framework import serializers
from rest_framework.relations import SlugRelatedField


from posts.models import Comment, Post, Group, Follow


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        read_only_fields = ('author',)
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = '__all__'
        read_only_fields = ('author', 'post')
        model = Comment


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Group


class FollowSerializer(serializers.ModelSerializer):
    user = SlugRelatedField(slug_field='username', read_only=True)
    following = SlugRelatedField(
        slug_field='username',
        source='author', read_only=True
    )

    class Meta:
        fields = ('user', 'following')
        read_only_fields = ('user',)
        model = Follow
