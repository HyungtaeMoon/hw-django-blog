from django.db import models

from bloguser.models import BlogUser


class Post(models.Model):
    user = models.ForeignKey(
        BlogUser,
        on_delete=models.CASCADE,
        related_name='my_post',
    )
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    @property
    def like_users(self):
        return [like.user for like in self.post_like.all()]

class PostLike(models.Model):
    post = models.ForeignKey(
        Post,
        related_name='post_like',
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        BlogUser,
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(auto_now_add=True)
