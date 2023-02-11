from django.db import models


class Products(models.Model):
    name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=150, decimal_places=2)
    score = models.IntegerField()
    image = models.ImageField(upload_to='Image/')



    def __str__(self):
        return self.name