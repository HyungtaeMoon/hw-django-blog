from django.db import models


class BlogUser(models.Model):
    name = models.CharField(max_length=40)
    friends = models.ManyToManyField(
        'self',
        related_name='my_friends',
    )
    block_users = models.ManyToManyField(
        'self',
        related_name='block_users',
    )

    def __str__(self):
        return self.name

    @property
    def my_comments(self):
        return self.comments.all()