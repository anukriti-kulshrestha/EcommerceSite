from django.db import models
from django.conf import settings

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8,decimal_places=2)
    description = models.CharField(max_length=300)
    image = models.ImageField(upload_to='uploads/',blank=True,null=True)
    CATEGORIES =(('E','Electronics'),('F','Fashion'),('B','Books'),('H','Household'))
    category = models.CharField(max_length=100,choices=CATEGORIES)
    stock = models.IntegerField()
    def __str__(self):
        return self.name
class OrderItems(models.Model):
    item = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=8,decimal_places=2,default=0)
    def __str__(self):
        return self.item.name

class Orders(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=8,decimal_places=2,default=0)
    items = models.ForeignKey(OrderItems,on_delete=models.CASCADE,null=True)
    ordered_date = models.DateTimeField(auto_now_add=True)
    ordered = models.BooleanField(default=False)
    def __str__(self):
        return settings.user.username

