from django.db import models

class Fund(models.Model):
    name= models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    risk_level = models.CharField(max_length=200)
    expense_ratio = models.CharField(max_length=200)
    returns_1yr = models.CharField(max_length=200)
    returns_3yr = models.CharField(max_length=200)

    def __str__(self):
        return self.name