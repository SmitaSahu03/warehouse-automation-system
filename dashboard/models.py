from tabnanny import verbose
from unicodedata import category
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

CATEGORY=(
    ('Stationary','Stationary'),
    ('Electronics','Electronics'),
    ('Food','Food'),
)

class Product(models.Model):
    name = models.CharField(max_length = 100 , null = True)
    category = models.CharField(max_length = 20, choices = CATEGORY , null = True)
    quantity = models.PositiveIntegerField(null = True)

    class Meta:
        verbose_name_plural = 'Product'

    def __str__(self):
        return f'{self.name}-{self.quantity}'

class Rack(models.Model):
    rack = models.CharField(max_length = 100, null = True)
    product = models.ForeignKey(Product, on_delete = models.CASCADE , null = True)
    
    rack_quantity = models.PositiveIntegerField(null=True)

    #class Meta:
     #   verbose_name_plural = 'Rack'

    def __str__(self):
        return f'{self.rack} {self.product}'



