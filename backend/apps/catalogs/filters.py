from django_filters import rest_framework as df
from .models import FilialPrice, Characterictic
from django.db.models import Subquery, OuterRef


class CatalogFilter(df.FilterSet):
    """
    Фильтрация для каталогов
    """
    filial_id = df.NumberFilter(field_name='filial_id__id')
    product_id = df.NumberFilter(field_name='product_id__id')
    characteristic_id = df.NumberFilter(method='by_products_characteristics')

    class Meta:
        model = FilialPrice
        fields = (
            "filial_id",
            "product_id",
            "characteristic_id",
        )

    @staticmethod
    def by_products_characteristics(queryset, name, value):
        return queryset.filter(product_id__in=Subquery(
            Characterictic.objects.select_related(
                'characterictic_id',
            ).prefetch_related(
                'products'
            ).filter(
                products__in=queryset.values_list("product_id", flat=True),
                pk=value
            ).values_list("products", flat=True)
        ))
