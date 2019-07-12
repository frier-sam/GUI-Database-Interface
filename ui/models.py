from django.db import models
# import datetime

# Create your models here.

class employee(models.Model):
    name = models.CharField(max_length=30)
    phone = models.IntegerField()
    city = models.CharField(max_length=60)
    state = models.CharField(max_length=30)
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    
    
class salary(models.Model):
    employee_id = models.ForeignKey(employee,on_delete=models.CASCADE)
    amount = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    deposition_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (self.amount)
