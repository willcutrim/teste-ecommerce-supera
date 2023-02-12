from rest_framework import viewsets
from .models import Carrinho

from .serializers import CarrinhoSerializer

class CarrinhoViewset(viewsets.ModelViewSet):
    queryset = Carrinho.objects.all()
    serializer_class = CarrinhoSerializer