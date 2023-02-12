from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from products.viewset import ProductsViewset

router = routers.DefaultRouter()
router.register('products', ProductsViewset)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('user/', include('user.urls')),
    path('shoppingcart/', include('shoppingcart.urls')),
    path('products/', include('products.urls')),

    path('api-auth/', include('rest_framework.urls')),

    path('api/', include(router.urls)),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
