from django.urls import path
from . import views

urlpatterns = [
    path('transactions/', views.transactions, name='transaction'),
    path('transactions/<str:Name>',views.itemTransactions,name='itemTransactions')
]