from django.urls import path

from .views import CreateProducts, ListProducts

urlpatterns = [
    path('create-products/', CreateProducts.as_view(), name='create-products'),
    path('list-products/<str:filtro>', ListProducts.as_view(), name='list-products'),
]