from django.db import models

# Create your models here.
class Inventory(models.Model):
    Name = models.CharField(default='Nil',max_length=255,unique=True,primary_key=True)
    Cost = models.IntegerField(default='0',null=True,blank=True)
    Quantity = models.IntegerField(default='0',null=True,blank=True )
    Quantity_sold = models.IntegerField(default='0' ,null=True,blank=True)
    Selling_price = models.IntegerField( default='0',null=True,blank=True)
    Profit_earned = models.IntegerField( default='0',null=True,blank=True)
    Revenue = models.IntegerField(default='0',null=True)

    class Meta:
        db_table = 'Inventory'
