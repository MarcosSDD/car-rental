from rest_framework import serializers
from api.models import Company, Client, Client_rent

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class Client_rentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client_rent
        fields = '__all__'

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