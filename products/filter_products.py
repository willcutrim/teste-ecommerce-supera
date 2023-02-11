from .serializers import ProductsSerializer
from .models import Products

from rest_framework.response import Response

def order_list(filtro):
    match filtro:
        case 'score-asc':
            products = Products.objects.order_by('-score')
            serializer = ProductsSerializer(products, many=True)
            return Response(serializer.data)
        case 'score-des':
            products = Products.objects.order_by('score')
            serializer = ProductsSerializer(products, many=True)
            return Response(serializer.data)
        case 'order-alpha':
            products = Products.objects.order_by('name')
            serializer = ProductsSerializer(products, many=True)
            return Response(serializer.data)
        case 'low-price':
            products = Products.objects.order_by('price')
            serializer = ProductsSerializer(products, many=True)
            return Response(serializer.data)
        case 'big-price':
            products = Products.objects.order_by('-price')
            serializer = ProductsSerializer(products, many=True)
            return Response(serializer.data)
        case 'all-products':
            products = Products.objects.all()
            serializer = ProductsSerializer(products, many=True)
            return Response(serializer.data)