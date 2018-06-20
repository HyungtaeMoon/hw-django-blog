from django.db import models


class UserInfo(models.Model):
    user = models.OneToOneField(
        'BlogUser',
        on_delete=models.CASCADE,
    )

    address = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)