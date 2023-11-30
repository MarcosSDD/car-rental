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
        fields = ["id_client", "id_company", "daily_cost", "days"]

class RentsCompanySerializer(serializers.Serializer):
    id_company = serializers.IntegerField()
    name_company = serializers.CharField()
    records_quantity = serializers.IntegerField()

class RentsClientSerializer(serializers.Serializer):
    id_client = serializers.IntegerField()
    name_client = serializers.CharField()
    records_quantity = serializers.IntegerField()

class CostClientSerializer(serializers.Serializer):
    id_client = serializers.IntegerField()
    name_client = serializers.CharField()
    total_cost = serializers.IntegerField()