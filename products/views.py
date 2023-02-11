from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from .serializers import ProductsSerializer

from .filter_products import order_list

class ListProducts(APIView):
    def get(self, request, filtro):
        return order_list(filtro)
            

class CreateProducts(APIView):
    def post(self, request):
        serializer = ProductsSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    