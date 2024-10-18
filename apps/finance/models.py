from django.db import models

class Product(models.Model):
    categories = [
        ('sa','Salt'),
        ('sw','Sweet')
    ]
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=2,choices=categories)
    description = models.TextField()
    def __str__(self):
        return self.name

class Order(models.Model):
    orderTypes = [
        ('tg','To go'),
        ('fh','For here')
    ]
    statuses = [
        ('oh','On hold'),
        ('op','On preparation'),
        ('se','Served')
    ]
    orderName = models.CharField(max_length=40,null=True)
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    amount = models.IntegerField()
    orderType = models.CharField(max_length=2,choices=orderTypes)
    status = models.CharField(max_length=2,choices=statuses,default='oh')
    date = models.DateField(auto_now=True)