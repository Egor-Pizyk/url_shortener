from django.contrib.auth.models import User
from django.db import models


class Url(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    link = models.CharField(max_length=10000)
    short_link = models.SlugField()
    counter = models.IntegerField(default=0)

    def __str__(self):
        return self.link
