from django.db import models

# Create your models here.
class Transactions(models.Model):
    Name = models.CharField(default=None,max_length=255)
    Item = models.ForeignKey('Inventory.Inventory',on_delete = models.CASCADE,default=None)
    Quantity = models.IntegerField(default='0',null=True,blank=True)
    Selling_price = models.IntegerField(default='0',null=True,blank=True)
    Transactiondttm = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Transactions'