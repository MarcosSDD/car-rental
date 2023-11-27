from django.db import models


class Company(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)

    def __str__(self) -> str:
        return f"{self.name}"


class Client(models.Model):
    id = models.IntegerField(primary_key=True)
    rut = models.CharField(max_length=15)
    name = models.CharField(max_length=100)
    active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"{self.name}"


class Client_rent(models.Model):
    id_cliente = models.ForeignKey(Client, to_field="id", on_delete=models.CASCADE)
    id_empresa = models.ForeignKey(Company, to_field="id", on_delete=models.CASCADE)
    costo_diario = models.IntegerField()
    dias = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.id_cliente}:{self.id_empresa}"