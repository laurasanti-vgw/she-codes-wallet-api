from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.http import Http404, HttpResponse
from .models import Wallet
from .serializers import WalletSerializer


class WalletBalance(APIView):

    def get_object(self, pk):
        try:
            wallet = Wallet.objects.get(pk=pk)
            return wallet
        except Wallet.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        wallet = self.get_object(pk)
        serializer = WalletSerializer(wallet)
        return Response(serializer.data)

class CreditWallet(APIView):

    def credit_wallet(wallet, request):
        payload=request.data
        
        wallet.transactionId = payload.get('transactionId')
        wallet.version = wallet.version + 1
        wallet.coins = wallet.coins + payload.get('coins')
        return wallet


    def post(self, request, pk):
        payload=request.data
        
        wallet = Wallet.objects.filter(pk=pk).first()
        serializer = WalletSerializer(wallet)

        if wallet is not None:
            wallet = self.credit_wallet(wallet, request)
                
        else:
            transactionId = payload.get('transactionId')
            version = 1
            coins = payload.get('coins')


        wallet, created = Wallet.objects.update_or_create(
            id=pk, defaults={'transactionId': transactionId, 'version': version, 'coins': coins },
        )
        serializer = WalletSerializer(wallet)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

