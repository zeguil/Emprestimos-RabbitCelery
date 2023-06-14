
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from propostas.viewsets import PropostaViewSet

router = DefaultRouter()
router.register('propostas', PropostaViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
