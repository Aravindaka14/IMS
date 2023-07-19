from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Inventory


# Create your views here.
def inventory(request):
    template = loader.get_template('inventory.html')
    inventoryData = Inventory.objects.all().values()
    totalProfits = 0;
    totalStocks = 0;
    highestCost = {
        "name": "",
        "cost": 0
    };
    highestProfits = {
        "name": "",
        "profits":0
    };
    mostSoldItem = {
        "name" :"",
        "quantitySold":0
    };

    for x in inventoryData:
        totalProfits += int(x["Profit_earned"]);
        totalStocks += int(x["Quantity"]);
        if x["Cost"] > highestCost["cost"]:
            highestCost["cost"] = x["Cost"];
            highestCost["name"] = x["Name"];
        if x["Profit_earned"] > highestProfits["profits"]:
            highestProfits["name"] = x["Name"];
            highestProfits["profits"] = x["Profit_earned"];
        if x["Quantity_sold"] > mostSoldItem["quantitySold"]:
            mostSoldItem["quantitySold"] = x["Quantity_sold"];
            mostSoldItem["name"] = x["Name"];

    context ={
        'inventoryData' : inventoryData,
        'totalProfit' : totalProfits,
        'totalStocks' : totalStocks,
        'highestCost' : highestCost,
        'highestProfits' : highestProfits,
        'mostSoldItem' : mostSoldItem
    };
    return HttpResponse(template.render(context,request))   