from django.contrib import admin
from api.models import Company, Client, Client_rent


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    pass


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    pass


@admin.register(Client_rent)
class Client_rentAdmin(admin.ModelAdmin):
    pass
