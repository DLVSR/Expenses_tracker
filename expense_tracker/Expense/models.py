from django.db import models

# Create your models here.
from django.db import models

class Expense(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50)
    date = models.DateField()

    def __str__(self):
        return f"{self.category} - {self.amount}"

