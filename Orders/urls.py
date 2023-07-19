from django.urls import path
from . import views


urlpatterns = [
    path('orders/',views.orders, name='orders'),
    path('orders/received/<int:id>',views.ordersReceived,name='ordersReceived'),
    path('orders/cancel/<int:id>',views.ordersCancel,name='ordersCancel'),
    path('orders/<str:Name>',views.itemOrders,name='itemOrders'),
    path('orders/received/<str:Name>',views.itemReceivedOrders,name='itemReceivedOrders'),
    path('orders/cancel/<str:Name>',views.itemCancelOrders,name='itemCancelOrders')
]