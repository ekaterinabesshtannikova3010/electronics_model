# from django.db import models
#
#
# class Supplier(models.Model):
#     name = models.CharField(max_length=255)
#     debt_to_supplier = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return self.name
#
#
# class NetworkNode(models.Model):
#     LEVEL_CHOICES = [
#         (0, 'Завод'),
#         (1, 'Розничная сеть'),
#         (2, 'Индивидуальный предприниматель'),
#     ]
#
#     name = models.CharField(max_length=255)
#     email = models.EmailField()
#     country = models.CharField(max_length=100)
#     city = models.CharField(max_length=100)
#     street = models.CharField(max_length=255)
#     house_number = models.CharField(max_length=10)
#     level = models.IntegerField(choices=LEVEL_CHOICES)
#     supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='nodes', null=True, blank=True)
#     debt_to_supplier = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return self.name
#
#
# class Product(models.Model):
#     name = models.CharField(max_length=255)
#     model = models.CharField(max_length=255)
#     release_date = models.DateField()
#     network_node = models.ForeignKey(NetworkNode, on_delete=models.CASCADE, related_name='products')
#
#     def __str__(self):
#         return f"{self.name} ({self.model})"
from django.db import models


class Enterprise(models.Model):
    LEVEL = (
        (0, "Завод"),
        (1, "Розничная сеть"),
        (2, "Индивидуальный предприниматель"),
    )

    name = models.CharField(
        max_length=255,
        verbose_name="Название",
        help_text="Укажите название"
    )
    email = models.EmailField(
        max_length=100,
        verbose_name="Почта",
        help_text="Укажите email"
    )
    country = models.CharField(
        max_length=100,
        verbose_name="Страна",
        help_text="Укажите страну"
    )
    city = models.CharField(
        max_length=100,
        verbose_name="Город",
        help_text="Укажите город"
    )
    street = models.CharField(
        max_length=100,
        verbose_name="Улица",
        help_text="Укажите улицу"
    )
    house_number = models.CharField(
        max_length=10,
        verbose_name="Номер дома",
        help_text="Укажите номер дома"
    )
    level = models.PositiveIntegerField(
        choices=LEVEL,
        verbose_name="Уровень сети",
        default=0
    )
    supplier = models.ForeignKey(
        'self',
        verbose_name="Поставщик",
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    debt = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.00,
        verbose_name="Задолженность",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Время и дата создания"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Звено сети"
        verbose_name_plural = "Звенья сети"


class Product(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Название продукта",
        help_text="Укажите название продукта"
    )
    model = models.CharField(
        max_length=255,
        verbose_name="Модель продукта",
        help_text="Укажите модель продукта"
    )
    release_date = models.DateField(
        verbose_name="Дата выхода продукта на рынок",
        help_text="Укажите дату выхода продукта на рынок"
    )
    supplier = models.ManyToManyField(
        Enterprise,
        verbose_name="Поставщик",
    )

    def __str__(self):
        return (f"{self.name} - {self.model}"
                f"Поставщик - {self.supplier}")

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
