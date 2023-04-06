from django.db import models

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=32)
    budget = models.FloatField()

    def __str__(self):
        return f"name={self.name},budget={self.budget}"

class Company(models.Model):
    client = models.ForeignKey(Client,on_delete=models.CASCADE)
    company_name = models.CharField(max_length=43)
    company_city = models.CharField(max_length=23)

    def __str__(self):
        return f"company_name={self.company_name},address={self.company_city}"