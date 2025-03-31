from rest_framework import viewsets, permissions
from .models import Supplier
from .serializers import SupplierSerializer


class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = [permissions.IsAuthenticated]  # Только активные сотрудники могут получить доступ

    def perform_update(self, serializer):
        # Запретить обновление поля "задолженность перед поставщиком"
        serializer.save(debt=serializer.instance.debt)

    def get_queryset(self):
        # Фильтрация объектов по стране
        queryset = super().get_queryset()
        country = self.request.query_params.get('country', None)
        if country is not None:
            queryset = queryset.filter(country=country)
        return queryset
