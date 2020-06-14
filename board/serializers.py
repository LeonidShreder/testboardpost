from rest_framework import serializers
from .models import Post, Comments


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ['content', 'author_name', 'comments_post']


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True)

    class Meta:
        model = Post
        fields = ['author_name', 'title', 'text', 'link', 'date',
                  'upVotes', 'comments']





