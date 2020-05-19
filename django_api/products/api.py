from .models import Products
from .serializers import ProductsSerializer
from rest_framework import viewsets, permissions
from rest_framework.parsers import MultiPartParser


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    parser_classes = [MultiPartParser]
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ProductsSerializer
