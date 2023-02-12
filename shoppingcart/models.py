from django.db import models
from django.contrib.auth.models import User
from products.models import Products

class Carrinho(models.Model):

    FRETE_CHOICES = (
        ('pagar', 'Pagar'),
        ('nao_pagar', 'Frete gratis')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Products, related_name='name_product')
    total_price = models.DecimalField(max_digits=150, decimal_places=2)
    frete = models.CharField(max_length=150, choices=FRETE_CHOICES)
    total_frete = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)
    date_of_purchase = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return '%s' % (self.user)