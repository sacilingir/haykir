from django.db import models

# Create your models here.

class Tweet(models.Model):
    nickname = models.CharField(max_length=50)
    mesage = models.CharField(max_length=50)

    def __str__(self):
        return f"Nick:{self.nickname} mesaj:{self.mesage}"
