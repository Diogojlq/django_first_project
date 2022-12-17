from django.db import models

# Create your models here.

class User(models.Model):
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=30)
    nick_name = models.CharField(max_length=25)

    def __str__(self):
        return f'{self.nick_name}, email : {self.email}, password : {self.password}'