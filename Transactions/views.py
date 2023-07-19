from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Transactions

# Create your views here.
def transactions(request):
    template = loader.get_template('transactions.html')
    soldData = Transactions.objects.all().values()
    context = {
        'soldData' : soldData
    }
    return HttpResponse(template.render(context,request))

def itemTransactions(request,Name):
    template = loader.get_template('transactions.html')
    soldData = Transactions.objects.filter(Item_id = Name)
    context ={
        'soldData' :soldData
    }
    return HttpResponse(template.render(context,request))