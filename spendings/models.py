from locale import currency
from django.db import models 
from django.core.validators import MinLengthValidator
class Spending(models.Model):
    description = models.CharField(max_length=255)
    amount = models.BigIntegerField()
    spent_at = models.DateTimeField()
    currency = models.CharField(max_length=3,validators=[MinLengthValidator(3)])