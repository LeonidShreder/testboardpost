from rest_framework import viewsets

from .models import Post, Comments
from .serializers import PostSerializer, CommentSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('date')
    serializer_class = PostSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comments.objects.all().order_by('creation_date')
    serializer_class = CommentSerializer
