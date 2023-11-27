from rest_framework import routers
from api.views import CompanyViewSet, ClientViewSet, Client_rentViewSet

router = routers.DefaultRouter()
router.register("empresas", viewset=CompanyViewSet, basename="empresas")
router.register("clientes",viewset=ClientViewSet,basename="clientes")
router.register("arriendos",viewset=Client_rentViewSet,basename="arriendos")