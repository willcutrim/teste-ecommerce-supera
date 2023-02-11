from rest_framework import viewsets
from .models import Products

from .serializers import ProductsSerializer

class ProductsViewset(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer