from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('<str:pk>/', views.WalletBalance.as_view()),
    path('<str:pk>/credit', views.CreditWallet.as_view()),
    path('<str:pk>/debit', views.DebitWallet.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)