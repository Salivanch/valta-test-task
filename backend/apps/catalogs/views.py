from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters import rest_framework as df

from .models import (
    FilialPrice,
    Characterictic
)
from .serializers import (
    FilialPriceSerializer,
    FilialPriceSimpleSerializer,
    CharactericticSerializer
)
from .filters import (
    CatalogFilter
)


class CatalogViewSet(viewsets.ModelViewSet):
    """
    Получение каталогов с товарами по различным фильтрам.
    Получение список характеристик по товару.
    """
    queryset = FilialPrice.objects.all()
    filter_backends = (df.DjangoFilterBackend,)
    filterset_class = CatalogFilter
    lookup_field = "product_id"

    serializer_actions = {
        'filial_products': FilialPriceSerializer,
        'filial_full_product': FilialPriceSerializer,
        'filial_product': FilialPriceSimpleSerializer,
        'product_characteristics': CharactericticSerializer,
        'characteristic_products': FilialPriceSerializer,
    }


    def get_serializer_class(self):
        return self.serializer_actions[self.action]

    @action(detail=False)
    def filial_products(self, request, *args, **kwargs):
        """Получить список объектов Product + стоимость для филиала"""
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


    @action(detail=True)
    def filial_full_product(self, request, *args, **kwargs):
        """Получить данные объекта Product + стоимость"""
        queryset = self.get_object()
        serializer = self.get_serializer(queryset)
        return Response(serializer.data)


    @action(detail=True)
    def filial_product(self, request, *args, **kwargs):
        """Получить данные объекта Product"""
        queryset = self.get_object()
        serializer = self.get_serializer(queryset)
        return Response(serializer.data)


    @action(detail=False)
    def product_characteristics(self, request, *args, **kwargs):
        """Получить список характеристик по товару"""
        product_id = self.kwargs.get("product_id", None)
        characterictics = Characterictic.objects.select_related(
            'characterictic_id'
        ).prefetch_related(
            'products'
        ).filter(products__in=[product_id])

        serializer = self.get_serializer(characterictics, many=True)
        return Response(serializer.data)
