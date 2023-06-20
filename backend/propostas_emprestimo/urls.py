
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from propostas.viewsets import PropostaViewSet
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register('propostas', PropostaViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
