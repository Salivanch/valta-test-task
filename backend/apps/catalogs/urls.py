from django.urls import path, include, re_path
from .views import CatalogViewSet

urlpatterns = [
    path('', CatalogViewSet.as_view({"get": "filial_products"})),
    path('<int:product_id>/', CatalogViewSet.as_view({"get": "filial_full_product"})),
    path('<int:product_id>/price/', CatalogViewSet.as_view({"get": "filial_product"})),
    path('<int:product_id>/characterictic/', CatalogViewSet.as_view({"get": "product_characteristics"})),
]
