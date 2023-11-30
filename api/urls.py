from django.urls import path, include
from rest_framework import routers
from .views import (
    CompanyViewSet,
    ClientViewSet,
    Client_rentViewSet,
    RentsCompanyView,
    RentsClientView,
    CostClientView
)

router = routers.DefaultRouter()
router.register(r"companys", viewset=CompanyViewSet, basename="companys")
router.register(r"clients",viewset=ClientViewSet,basename="clients")
router.register(r"rents",viewset=Client_rentViewSet,basename="rents")

urlpatterns = [
    path('rents-companys/', RentsCompanyView.as_view(), name='rents-companys'),
    path('rents-clients/', RentsClientView.as_view(), name='rents-clients'),
    path('cost-clients/', CostClientView.as_view(), name='cost-clients'),
] + router.urls