from django.db import models

# Create your models here.
class UserClaims(models.Model):
    username = models.CharField(max_length=100)
    id_token = models.CharField(max_length=1500)