from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserModel(models.Model):

    
    BelongTo = models.OneToOneField(User, default = None)
    HuntCompleted = models.TextField(default = "[]", blank = True)
    HuntInProgress = models.TextField(default = "[]", blank = True)

    def __str__(self):
        return self.FirstName + " " + self.LastName
