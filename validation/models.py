from django.db import models
from django.contrib.auth.models import User

class Validation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=50)
    birth_date= models.DateTimeField()
    cpf = models.CharField(max_length=11)
    rg = models.CharField(max_length=13)
    cel = models.CharField(max_length=14)
    adress = models.CharField(max_length=50)
    number = models.CharField(max_length=4)
    distric = models.CharField(max_length=30)
    estate = models.CharField(max_length=20)
    profile_picture = models.ImageField(upload_to='images/users')
    profile_validation = models.ImageField(upload_to='images/validation')
