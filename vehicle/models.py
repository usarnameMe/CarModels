from django.db import models


class Vehicle(models.Model):
    objects = None
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    comments = models.TextField(blank=True)

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"
