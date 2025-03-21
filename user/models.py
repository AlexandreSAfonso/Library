from django.db import models

class User(models.Model):
    user_name = models.CharField(max_length=30)
    user_email = models.EmailField()
    user_password = models.CharField(max_length=64)

    def __str__(self) -> str:
        return self.user_name