from .models import Categories
from .serializers import CategoriesSerializer
from rest_framework import viewsets, permissions


class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CategoriesSerializer
