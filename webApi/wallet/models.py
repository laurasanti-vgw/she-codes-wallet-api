from django.db import models

class Wallet(models.Model):
    id = models.CharField(max_length=200, primary_key=True)
    transactionId = models.CharField(max_length=200)
    version = models.IntegerField(null=True)
    coins = models.IntegerField()
