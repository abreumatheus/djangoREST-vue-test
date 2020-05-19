from rest_framework import routers
from categories.api import CategoriesViewSet
from products.api import ProductViewSet


router = routers.DefaultRouter()
router.register('categories', CategoriesViewSet, 'Categories')
router.register('products', ProductViewSet, 'Products')
