from django.urls import path
from . import views

urlpatterns =[
    path('items/', views.items, name='items'),
    path('items/add/<str:Name>',views.addItem, name='addItem'),
    path('items/sell/<str:Name>',views.sellItem, name='sellItem'),
    path('items/view/<str:Name>',views.viewItem, name='viewItem'),
    path('items/create',views.createItem, name='createItem'),
    # path('orders/',views.orderPlaced, name='orderPlaced')
]