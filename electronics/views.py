# from rest_framework import viewsets, permissions
# from .models import Supplier
# from .serializers import SupplierSerializer
#
#
# class SupplierViewSet(viewsets.ModelViewSet):
#     queryset = Supplier.objects.all()
#     serializer_class = SupplierSerializer
#     permission_classes = [permissions.IsAuthenticated]  # Только активные сотрудники могут получить доступ
#
#     def perform_update(self, serializer):
#         # Запретить обновление поля "задолженность перед поставщиком"
#         serializer.save(debt=serializer.instance.debt)
#
#     def get_queryset(self):
#         # Фильтрация объектов по стране
#         queryset = super().get_queryset()
#         country = self.request.query_params.get('country', None)
#         if country is not None:
#             queryset = queryset.filter(country=country)
#         return queryset
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import (CreateAPIView, RetrieveAPIView, ListAPIView, UpdateAPIView, DestroyAPIView)
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from electronics.models import Enterprise, Product
from electronics.permissions import IsActive
from electronics.serializers import EnterpriseSerializer, ProductSerializer


# Enterprises ##################################################################
class EnterpriseCreateAPIView(CreateAPIView):
    queryset = Enterprise.objects.all()
    serializer_class = EnterpriseSerializer
    permission_classes = [IsAuthenticated, IsActive]


class EnterpriseRetrieveAPIView(RetrieveAPIView):
    queryset = Enterprise.objects.all()
    serializer_class = EnterpriseSerializer
    permission_classes = [IsAuthenticated, IsActive]


class EnterpriseListAPIView(ListAPIView):
    queryset = Enterprise.objects.all()
    serializer_class = EnterpriseSerializer
    permission_classes = [IsAuthenticated, IsActive]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['country', 'city', 'street', 'house_number', 'level']


class EnterpriseUpdateAPIView(UpdateAPIView):
    queryset = Enterprise.objects.all()
    serializer_class = EnterpriseSerializer
    permission_classes = [IsAuthenticated, IsActive]

    def perform_update(self, serializer):
        if "debt" in serializer.validated_data:
            serializer.validated_data.pop("debt")
            raise Exception("Невозможно изменить поле задолженности")
        super().perform_update(serializer)


class EnterpriseDestroyAPIView(DestroyAPIView):
    queryset = Enterprise.objects.all()
    serializer_class = EnterpriseSerializer
    permission_classes = [IsAuthenticated, IsActive]


# Products #####################################################################
class ProductCreateAPIView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsActive]


class ProductRetrieveAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsActive]


class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsActive]


class ProductUpdateAPIView(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsActive]


class ProductDestroyAPIView(DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsActive]