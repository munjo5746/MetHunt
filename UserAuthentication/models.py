from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserModel(models.Model):

    User = models.OneToOneField(User, default = None)
    HuntCompleted = models.TextField(default = "[]")
    HuntInProgress = models.TextField(default = "[]")

    def __str__(self):
        return self.FirstName + " " + self.LastName
