from django.db import models

# Create your models here.
class UserModel(models.Model):

    UserName = models.CharField(max_length = 50)
    Email = models.EmailField(unique = True)
    FirstName = models.CharField(max_length = 50, default = "")
    LastName = models.CharField(max_length = 50, default = "")
    Password = models.CharField(max_length = 100, default = "")

    def __str__(self):
        return self.FirstName + " " + self.LastName
