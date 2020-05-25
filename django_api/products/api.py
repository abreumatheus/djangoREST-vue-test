from .models import Products
from .serializers import ProductsSerializer
from rest_framework import viewsets, permissions
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from datetime import datetime


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    parser_classes = [MultiPartParser]
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ProductsSerializer

    def list(self, request, *args, **kwargs):
        products = Products.objects.filter(deleted_at=None).all()
        return Response(ProductsSerializer(products, many=True).data)

    def destroy(self, request, *args, **kwargs):
        product = self.get_object()
        product.deleted_at = datetime.utcnow()
        product.save()
        return Response(ProductsSerializer(product).data)
