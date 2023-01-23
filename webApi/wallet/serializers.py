from rest_framework import serializers

class WalletSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    transactionId = serializers.CharField(max_length=200)
    version = serializers.IntegerField()
    coins = serializers.IntegerField()