from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from api.models import Company, Client, Client_rent
from api.serializers import CompanySerializer, ClientSerializer, Client_rentSerializer


class CompanyViewSet(ModelViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()

#class CompanyUpdateView()

class ClientViewSet(ModelViewSet):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()

class Client_rentViewSet(ModelViewSet):
    serializer_class = Client_rentSerializer
    queryset = Client_rent.objects.all()