from rest_framework import serializers

class WalletSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    coins = serializers.IntegerField()