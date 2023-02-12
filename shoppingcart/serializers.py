from rest_framework import serializers
from .models import Carrinho


class CarrinhoSerializerList(serializers.ModelSerializer):
    products = serializers.StringRelatedField(many=True, read_only=True)
    user = serializers.StringRelatedField(source='user.username', read_only=True)


    class Meta:
        model = Carrinho
        fields = '__all__'



class CarrinhoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrinho
        fields = '__all__'