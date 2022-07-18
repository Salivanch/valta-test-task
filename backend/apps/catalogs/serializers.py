from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField

from .models import (
    Product,
    Filial,
    Characterictic,
    FilialPrice
)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            '__all__'
        )


class FilialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filial
        fields = (
            '__all__'
        )


class CharactericticSerializer(serializers.ModelSerializer):
    characterictic_id = RecursiveField()

    class Meta:
        model = Characterictic
        exclude = ('products',)


class FilialPriceSerializer(serializers.ModelSerializer):
    product_id = ProductSerializer()
    filial_id = FilialSerializer()

    class Meta:
        model = FilialPrice
        fields = (
            '__all__'
        )

class FilialPriceSimpleSerializer(serializers.ModelSerializer):
    product_id = ProductSerializer()
    filial_id = FilialSerializer()

    class Meta:
        model = FilialPrice
        exclude = ['price']