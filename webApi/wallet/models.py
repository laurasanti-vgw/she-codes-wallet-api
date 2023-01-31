from django.db import models

class Wallet(models.Model):
    id = models.IntegerField(primary_key=True)
    coins = models.IntegerField()
