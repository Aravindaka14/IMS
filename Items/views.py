from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from django.template import loader
from Inventory.models import Inventory
from Transactions.models import Transactions
from Orders.models import Orders
from .createItemForm import CreateForm


# Create your views here.
def items(request):
    template = loader.get_template('items.html')
    itemData = Inventory.objects.all().values()
    context ={
        'itemData' : itemData
    }
    return HttpResponse(template.render(context,request));


def addItem(request,Name):
    if request.method == "POST":
        if int(request.POST['quantity']) <1: 
            messages.warning(request,'Quantity must be greater than 0')
            return redirect(request.META.get('HTTP_REFERER')) 
        itemData = Inventory.objects.get(Name = Name)
        orderData = Orders()
        orderData.Name = request.POST['person_name']
        orderData.Item = Inventory.objects.get(Name = Name)
        orderData.Quantity = request.POST['quantity']
        orderData.Cost = itemData.Cost
        orderData.save()
        return redirect('/orders')
    else:    
        template = loader.get_template('addItem.html');
        itemData = Inventory.objects.get(Name = Name);
        context ={
        'itemData' : itemData
        }
        return HttpResponse(template.render(context,request));


def sellItem(request,Name):
    if request.method == "POST":
        if int(request.POST['quantity']) < 0: 
            messages.warning(request,'Quantity must be greater than 0')
            return redirect(request.META.get('HTTP_REFERER'))
        itemData = Inventory.objects.get(Name = Name)
        if itemData.Quantity < int(request.POST['quantity']):
            messages.warning(request,'Not Enough Stocks!')
            # return redirect('/items/sell/{{<str:Name>}}')
            return redirect(request.META.get('HTTP_REFERER'))
        else:    
            itemData.Quantity -= int(request.POST['quantity']) 
            itemData.Quantity_sold += int(request.POST['quantity'])
            itemData.Revenue = itemData.Quantity_sold * itemData.Selling_price
            itemData.Profit_earned = itemData.Revenue - (itemData.Cost * itemData.Quantity_sold)
            itemData.save()

        transData = Transactions()
        transData.Name = request.POST['person_name']
        transData.Item = Inventory.objects.get(Name = Name)
        transData.Quantity = request.POST['quantity']
        transData.Selling_price = itemData.Selling_price
        transData.save()
        return redirect('/transactions')  
    else:
        template = loader.get_template('sellItem.html')
        itemData = Inventory.objects.get(Name = Name)
        context ={
        'itemData' : itemData
        }
        return HttpResponse(template.render(context,request));


def viewItem(request,Name):
    template = loader.get_template('viewItem.html');
    itemData = Inventory.objects.get(Name = Name)
    context ={
        'itemData' : itemData
    }
    return HttpResponse(template.render(context,request));


def createItem(request):
    if request.method == "POST":
        if Inventory.objects.filter(Name = request.POST['Name']).exists():
            messages.warning(request,'Stock already exist! Please try with different name')
            return redirect(request.META.get('HTTP_REFERER'))
        elif int(request.POST['Cost']) < 1 or int(request.POST['Selling_price']) < 1:
            messages.warning(request,'Cost and Selling price must be greater than 0')
            return redirect(request.META.get('HTTP_REFERER'))
        elif int(request.POST['Cost']) > int(request.POST['Selling_price']): 
            messages.warning(request,'Selling price must be greater than Cost price')
            return redirect(request.META.get('HTTP_REFERER'))   
        else:
            form = CreateForm(request.POST)
            if form.is_valid():
                form.save()
            return redirect('/items')
    else:    
        template = loader.get_template('createItem.html')
        context = {
        'form': CreateForm()
        }    
        return HttpResponse(template.render(context,request))
