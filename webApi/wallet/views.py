from rest_framework.views import APIView
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
