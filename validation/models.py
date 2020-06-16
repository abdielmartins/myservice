from django.db import models
from django.contrib.auth.models import User

class Validation(models.Model):
    uservalid = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=50)
    birth_date= models.CharField (max_length=10)
    cpf = models.CharField(max_length=11)
    rg = models.CharField(max_length=9, default='123456789' )
    cel = models.CharField(max_length=14, default='41 123451234')
    cep = models.CharField(max_length=9, default='12345-123')
    adress = models.CharField(max_length=50, default='Rua: 123')
    num = models.CharField(max_length=4, default='123')
    district = models.CharField(max_length=30, default='Centro')
    city = models.CharField(max_length=30, default='Curitiba')
    state = models.CharField(max_length=20, default='Parana')
    profile_picture = models.ImageField(upload_to='images/users')
    profile_validation = models.ImageField(upload_to='images/validation')