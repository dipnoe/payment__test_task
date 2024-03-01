from django.db import models


# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        ordering = ['name', 'price', ]

    def __str__(self):
        return self.name
