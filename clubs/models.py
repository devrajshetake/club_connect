from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=500, )
    postImage = models.ImageField(null = True)
    desc = models.TextField(null = True)
