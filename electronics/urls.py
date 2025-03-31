from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .apps import ElectronicsConfig
from .views import SupplierViewSet

app_name = ElectronicsConfig.name

router = DefaultRouter()
router.register(r'suppliers', SupplierViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
