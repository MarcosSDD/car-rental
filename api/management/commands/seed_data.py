import json
from django.core.management.base import BaseCommand
from api.models import Company, Client, Client_rent  

class Command(BaseCommand):
    help = 'Seed the database with data from a JSON file'

    def handle(self, *args, **kwargs):
        self.run_seed(self.get_json_data_to_file('json_files/empresas.json'), Company)
        self.run_seed(self.get_json_data_to_file('json_files/clientes.json'),  Client)
        data_client_rent = self.create_client_rent(self.get_json_data_to_file('json_files/arriendos.json'))
        self.run_seed(data_client_rent, Client_rent)

        self.stdout.write(self.style.SUCCESS('Data seeding completed'))
    
    def create_client_rent(self, data):
        client_rent_array=[] 
        for entry in data:
            client_rent = {
                "id" : entry['id'],
                "id_cliente" : Client.objects.get(id=str(entry['id_cliente'])),
                "id_empresa" : Company.objects.get(id=str(entry['id_empresa'])),
                "costo_diario" : entry['costo_diario'],
                "dias" : entry['dias']
            }
            client_rent_array.append(client_rent)
        return client_rent_array
        
    def get_json_data_to_file(self, filePath):
        with open(filePath) as fileJson:
            return json.load(fileJson)

    def run_seed(self, data, model):
        for entry in data:
            model.objects.update_or_create(pk=entry['id'], defaults=entry)