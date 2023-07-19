from django import forms
from django.forms import ModelForm
from Inventory.models import Inventory

    
class CreateForm(ModelForm):
    class Meta:
        model = Inventory
        fields = ('Name','Cost','Selling_price')