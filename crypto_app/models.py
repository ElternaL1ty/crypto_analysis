from django.contrib.auth.models import AbstractUser
from djongo import models


class Crypto(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class CryptoUser(AbstractUser):
    crypto_list = models.ArrayField(model_container=Crypto)