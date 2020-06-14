from django.db import models
from django.contrib.auth.models import User

class Validation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=50)
    birth_date= models.DateTimeField()
    cpf = models.CharField(max_length=11)
    profile_picture = models.ImageField(upload_to='images/users')
    profile_validation = models.ImageField(upload_to='images/validation')
