from django.db import models

# Create your models here.
class UserModel(models.Model):
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)