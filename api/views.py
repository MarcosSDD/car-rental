from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from api.models import Company, Client, Client_rent
from django.db.models import Count, Sum
from api.serializers import (
    CompanySerializer,
    ClientSerializer, 
    Client_rentSerializer,
    RentsCompanySerializer,
    RentsClientSerializer,
    CostClientSerializer
)

class CompanyViewSet(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class ClientViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class Client_rentViewSet(ModelViewSet):
    queryset = Client_rent.objects.all()
    serializer_class = Client_rentSerializer

class RentsCompanyView(generics.ListAPIView):
    queryset = Company.objects.all()
    serializer_class = RentsCompanySerializer

    def list(self, request, *args, **kwargs):
        companys = Company.objects.values('id', 'name')
        rents = Client_rent.objects.values('id_company').annotate(records_quantity=Count('id'))
        results = []
        for company in companys:
            company_id = company['id']
            records_quantity = next((rent['records_quantity'] for rent in rents if rent['id_company'] == company_id), 0)
            results.append({'id_company': company_id, 'name_company': company['name'], 'records_quantity': records_quantity})

        serializer = self.get_serializer(results, many=True)
        return Response(serializer.data)

class RentsClientView(generics.ListAPIView):
    queryset = Client.objects.all()
    serializer_class = RentsClientSerializer

    def list(self, request, *args, **kwargs):
        clients = Client.objects.values('id', 'name')
        rents = Client_rent.objects.values('id_client').annotate(records_quantity=Count('id'))
        results = []
        for client in clients:
            client_id = client['id']
            records_quantity = next((rent['records_quantity'] for rent in rents if rent['id_client'] == client_id), 0)
            results.append({'id_client': client_id, 'name_client': client['name'], 'records_quantity': records_quantity})

        serializer = self.get_serializer(results, many=True)
        return Response(serializer.data)

class CostClientView(generics.ListAPIView):
    queryset = Client.objects.all()
    serializer_class = CostClientSerializer

    def list(self, request, *args, **kwargs):
        clients = Client.objects.values('id', 'name')
        costs = Client_rent.objects.values('id_client').annotate(total_cost=Sum('daily_cost'))
        results = []
        for client in clients:
            client_id = client['id']
            total_cost = next((cost['total_cost'] for cost in costs if cost['id_client'] == client_id), 0)
            results.append({'id_client': client_id, 'name_client': client['name'], 'total_cost': total_cost})

        serializer = self.get_serializer(results, many=True)
        return Response(serializer.data)