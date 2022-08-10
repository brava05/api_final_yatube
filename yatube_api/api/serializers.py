from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from django.contrib.auth import get_user_model

from posts.models import Comment, Post, Group, Follow

User = get_user_model()


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        read_only_fields = ('author',)
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
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
        read_only=False,
        queryset=User.objects.all()
    )

    def validate(self, data):
        user = self.context['request'].user
        following = data.get("following")
        if Follow.objects.filter(
            user=user,
            following=following
        ).exists():
            raise serializers.ValidationError('Такая подписка уже есть')

        if user == following:
            raise serializers.ValidationError(
                'Нельзя подписаться на самого себя')

        return data

    class Meta:
        fields = ('user', 'following')
        read_only_fields = ('user',)
        model = Follow
