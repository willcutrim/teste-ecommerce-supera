from django.urls import path
from .views import CarrinhoListView, CarrinhoPostView, CarrinhoHistoryView

urlpatterns = [
    path('carrinho-list/', CarrinhoListView.as_view(), name='carrinho-list'),
    path('carrinho-post/', CarrinhoPostView.as_view(), name='carrinho-post'),
    path('carrinho-mylist/<str:user>', CarrinhoHistoryView.as_view(), name='carrinho-post'),
]