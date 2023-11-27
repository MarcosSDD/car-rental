from rest_framework import serializers
from api.models import Company, Client, Client_rent

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ["id", "name"]

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ["id", "rut", "name", "active"]

class Client_rentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client_rent
        fields = ["id_cliente", "id_empresa", "costo_diario", "dias"]
        #fields = "__all__"