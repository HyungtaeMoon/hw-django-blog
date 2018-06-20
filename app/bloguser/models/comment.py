from django.db import models

from bloguser.models import BlogUser
from bloguser.models.post import Post


class Comment(models.Model):
    comment = models.TextField(max_length=20)
    user = models.ForeignKey(
        BlogUser,
        on_delete=models.CASCADE,
        related_name='comments',
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='posts',
    )
    created_at =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment


class CommentLike(models.Model):
    commentlike = models.ForeignKey(
        Comment,
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        BlogUser,
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(auto_now_add=True)