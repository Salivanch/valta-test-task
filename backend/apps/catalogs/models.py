from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=150)

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return self.name


class Filial(models.Model):
    name = models.CharField(max_length=50)
    region = models.PositiveIntegerField()

    class Meta:
        verbose_name = "Регион"
        verbose_name_plural = "Регионы"

    def __str__(self):
        return self.name


class Characterictic(models.Model):
    name = models.CharField(max_length=150)
    characterictic_id = models.ForeignKey("self", on_delete=models.SET_NULL, blank=True, null=True)
    products = models.ManyToManyField(Product, related_name='product', blank=True)

    class Meta:
        verbose_name = "Характеристика"
        verbose_name_plural = "Характеристики"

    def __str__(self):
        return self.name


class FilialPrice(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    filial_id = models.ForeignKey(Filial, on_delete=models.SET_NULL, blank=True, null=True)
    price = models.PositiveIntegerField()

    class Meta:
        verbose_name = "Цена"
        verbose_name_plural = "Цены"

    def __str__(self):
        return f"{self.filial_id.name} - {self.product_id.name} - {self.price}"
