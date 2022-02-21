from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    college = models.CharField(max_length=100)
    is_club_admin = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.user.first_name} : {self.code}"

    