from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Carrinho
from .serializers import CarrinhoSerializer, CarrinhoSerializerList



class CarrinhoListView(APIView):
    def get(self, request):
        carrinho_list = Carrinho.objects.all()
        serializer = CarrinhoSerializerList(carrinho_list, many=True)
        return Response(serializer.data)


class CarrinhoPostView(APIView):
    def post(self, request):
        serializer = CarrinhoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

 
class CarrinhoHistoryView(APIView):
    def get(self, request, user):
            carrinho_list = Carrinho.objects.filter(user=user)
            serializer = CarrinhoSerializer(carrinho_list, many=True)
            return Response(serializer.data)
    