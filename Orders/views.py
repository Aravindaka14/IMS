from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from .models import Orders
from Inventory.models import Inventory


# Create your views here.
def orders(request):
    template = loader.get_template('orders.html')
    orderData = Orders.objects.filter(Is_received = False , Is_cancel = False)
    context = {
        'orderData' : orderData
    }
    return HttpResponse(template.render(context,request))


def ordersReceived(request,id):
    if id != 0 :
        orderData = Orders.objects.get(id =id)
        orderData.Is_received = True
        orderData.save()
        updateOrder = Inventory.objects.get(Name = orderData.Item_id)
        updateOrder.Quantity += orderData.Quantity
        updateOrder.save()
        receivedData = Orders.objects.filter(Is_received = True)
        template = loader.get_template('orderReceived.html')
        context ={
            'receivedData': receivedData
        }
        return HttpResponse(template.render(context,request)) 
    else:
        receivedData = Orders.objects.filter(Is_received = True)
        template = loader.get_template('orderReceived.html')
        context ={
        'receivedData': receivedData
        }
        return HttpResponse(template.render(context,request))

def ordersCancel(request,id):
    if id != 0 :
        orderData = Orders.objects.get(id = id)
        orderData.Is_cancel = True
        orderData.save()
        cancelData = Orders.objects.filter(Is_cancel = True)
        template = loader.get_template('orderCancelled.html')
        context ={
            'cancelData':cancelData
        }
        return HttpResponse(template.render(context,request))
    else:
        cancelData = Orders.objects.filter(Is_cancel = True)
        template = loader.get_template('orderCancelled.html')
        context ={
            'cancelData':cancelData
        }
        return HttpResponse(template.render(context,request))
    

def itemOrders(request,Name):
    orderData = Orders.objects.filter(Item_id = Name , Is_received = False , Is_cancel = False)
    template = loader.get_template('orders.html')
    context = {
        'orderData' : orderData
    }
    return HttpResponse(template.render(context,request))


def itemReceivedOrders(request,Name):
    orderData = Orders.objects.filter(Item_id = Name , Is_received = True)
    template = loader.get_template('orderReceived.html')
    context = {
        'receivedData' : orderData
    }
    return HttpResponse(template.render(context,request))


def itemCancelOrders(request,Name):
    orderData = Orders.objects.filter(Item_id = Name , Is_cancel = True)
    template = loader.get_template('orderCancelled.html')
    context = {
        'cancelData' : orderData
    }
    return HttpResponse(template.render(context,request))