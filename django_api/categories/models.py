from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=255, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True, default=None)
    updated_at = models.DateTimeField(auto_now=True, null=True)
