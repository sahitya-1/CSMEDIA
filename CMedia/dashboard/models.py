from django.db import models

#from dashboard.models import CATEGORY_CHOICES
CATEGORY_CHOICES = (
    ('A','All Items'),
    ('M', 'Cookies,Deserts'),
    ('BW', 'Vegetables,Fruits'),
    ('TW', 'Soft Drinks'),
)


class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    brand = models.CharField(max_length=100)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=50)

# Create your models here.
