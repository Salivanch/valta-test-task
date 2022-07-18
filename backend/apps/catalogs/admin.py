from django.contrib import admin

from .models import (
    Product,
    Filial,
    Characterictic,
    FilialPrice
)


admin.site.register(Product)
admin.site.register(Filial)
admin.site.register(Characterictic)
admin.site.register(FilialPrice)
