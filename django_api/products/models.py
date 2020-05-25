from django.db import models
from categories.models import Categories


class Products(models.Model):
    name = models.CharField(max_length=255, null=False)
    description = models.TextField(null=False)
    price = models.FloatField(null=False)
    promotional_price = models.FloatField(null=True, default=None)
    photo = models.ImageField(upload_to='products/', max_length=None)
    category = models.ForeignKey(Categories, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True, default=None)
    updated_at = models.DateTimeField(auto_now=True, null=True)
