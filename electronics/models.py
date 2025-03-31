from django.db import models


class Supplier(models.Model):
    name = models.CharField(max_length=255)
    debt_to_supplier = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class NetworkNode(models.Model):
    LEVEL_CHOICES = [
        (0, 'Завод'),
        (1, 'Розничная сеть'),
        (2, 'Индивидуальный предприниматель'),
    ]

    name = models.CharField(max_length=255)
    email = models.EmailField()
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=255)
    house_number = models.CharField(max_length=10)
    level = models.IntegerField(choices=LEVEL_CHOICES)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='nodes', null=True, blank=True)
    debt_to_supplier = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    release_date = models.DateField()
    network_node = models.ForeignKey(NetworkNode, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return f"{self.name} ({self.model})"
