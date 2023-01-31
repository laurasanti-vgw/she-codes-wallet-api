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

    def credit_wallet(self, wallet, request):
        payload=request.data
        
        wallet.coins += payload.get('coins')
        wallet.save()
        return wallet


    def post(self, request, pk):
        
        wallet = Wallet.objects.filter(pk=pk).first()

        if wallet is None:
            wallet, created = Wallet.objects.update_or_create(
            id=pk, defaults={'coins': 0}
            )
 
        credited_wallet = self.credit_wallet(wallet, request)

        serializer = WalletSerializer(credited_wallet)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class DebitWallet(APIView):

    def get_object(self, pk):
        try:
            wallet = Wallet.objects.get(pk=pk)
            return wallet
        except Wallet.DoesNotExist:
            raise Http404


    def post(self, request, pk):
        payload=request.data

        wallet = self.get_object(pk)
        serializer = WalletSerializer(wallet)

        if wallet and self.overdrawn(wallet, request):
            return Response(f"You don't have enough coins in your wallet to debit {payload.get('coins')}", status=status.HTTP_400_BAD_REQUEST)
            
        wallet = self.debit_wallet(wallet, request)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    
    def overdrawn(self, wallet, request):
        payload=request.data

        current_balance = wallet.coins
        debit_request = payload.get('coins')

        if current_balance - debit_request < 0:
            return True
        return False


    def debit_wallet(self, wallet, request):
        payload=request.data
        
        wallet.coins = wallet.coins - payload.get('coins')
        wallet.save()
        return wallet
    





