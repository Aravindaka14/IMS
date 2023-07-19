from django.db import models

# Create your models here.
class Orders(models.Model):
    Name = models.CharField(default=None,max_length =255)
    Item  = models.ForeignKey('Inventory.Inventory',on_delete = models.CASCADE,default=None)
    Quantity = models.IntegerField(default='0',null=True,blank=True)
    Cost = models.IntegerField(default='0',null=True,blank=True)
    Orderdttm = models.DateTimeField(auto_now_add=True)
    Is_received = models.BooleanField(default=False)
    Is_cancel = models.BooleanField(default=False)

    class Meta:
        db_table = 'Orders'