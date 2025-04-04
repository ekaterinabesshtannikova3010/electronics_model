# from rest_framework import serializers
# from .models import Supplier
#
#
# class SupplierSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Supplier
#         fields = ['id', 'name', 'debt_to_supplier']
from rest_framework.serializers import ModelSerializer

from electronics.models import Enterprise, Product


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class EnterpriseSerializer(ModelSerializer):
    class Meta:
        model = Enterprise
        fields = "__all__"
