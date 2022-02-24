from statistics import mode
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    college = models.CharField(max_length=100, null=True)
    mobile = models.CharField(max_length=10,null=True)

    is_club_admin = models.BooleanField(default=False)


    def __str__(self):
        return self.user.first_name

    