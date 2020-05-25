from .models import Categories
from .serializers import CategoriesSerializer
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from datetime import datetime


class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CategoriesSerializer

    def list(self, request, *args, **kwargs):
        categories = Categories.objects.filter(deleted_at=None).all()
        return Response(CategoriesSerializer(categories, many=True).data)

    def destroy(self, request, *args, **kwargs):
        category = self.get_object()
        category.deleted_at = datetime.utcnow()
        category.save()
        return Response(CategoriesSerializer(category).data)
