from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from rest_framework import permissions

from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static

from valta import settings


schema_view = get_schema_view(
    openapi.Info(
        title="Test task API",
        default_version='v1',
        description="Test task API for valta",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('catalog/', include('apps.catalogs.urls')),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
