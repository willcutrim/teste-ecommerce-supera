from django.urls import path
from .views import UserApiView, LoginView

urlpatterns = [
    path('', UserApiView.as_view(), name='index'),
    path('login/', LoginView.as_view(), name='login'),
]