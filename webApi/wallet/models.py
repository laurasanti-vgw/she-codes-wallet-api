from django.db import models

class Wallet(models.Model):
    id = models.IntegerField(max_length=200, primary_key=True)
    coins = models.IntegerField()
