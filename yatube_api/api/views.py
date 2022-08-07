from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.throttling import AnonRateThrottle
from django.contrib.auth import get_user_model

from posts.models import Post, Comment, Group, Follow
from .serializers import PostSerializer, CommentSerializer
from .serializers import GroupSerializer, FollowSerializer
from .permissions import AuthorOrReadOnly, UserOrReadOnly

User = get_user_model()


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (AuthorOrReadOnly,)
    throttle_classes = (AnonRateThrottle,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (AuthorOrReadOnly,)

    def get_queryset(self):
        post = get_object_or_404(Post, pk=self.kwargs.get("post_id"))
        comments = Comment.objects.filter(post=post)
        return comments

    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=self.kwargs.get("post_id"))
        serializer.save(post=post, author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class FollowViewSet(viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = (UserOrReadOnly,)

    def get_queryset(self):
        folows = Follow.objects.filter(user=self.request.user)
        return folows

    def perform_create(self, serializer):
        author = get_object_or_404(
            User,
            username=self.request.data.get("following")
        )
        serializer.save(user=self.request.user, author=author)
