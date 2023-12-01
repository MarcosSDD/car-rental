from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from api.models import Company, Client, Client_rent

class ApiViewSetTest(TestCase):
    def setUp(self):
        self.username = "dev"
        self.email = "dev@gmail.com"
        self.password = "password"
        self.user = User.objects.create_user(self.username, self.email, self.password)
        token = Token.objects.create(user=self.user).key
        self.company = Company.objects.create(name="myCompany")
        self.apiclient = APIClient()
        self.apiclient.credentials(HTTP_AUTHORIZATION="Token {}".format(token))
        self.user = Client.objects.create(rut="1111111-1", name="user", active=True)
        self.rent = Client_rent.objects.create(
            id_client =  Client.objects.get(id="1"),
            id_company =  Company.objects.get(id="1"),
            daily_cost =  "1500",
            days =  "3"
        )

    def test_list_company(self):
        response = self.apiclient.get('/api/companys/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            [
                {
                    "id": 1,
                    "name": "myCompany"
                },
            ]
        )
    
    def test_list_client(self):
        response = self.apiclient.get('/api/clients/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            [
                {
                    "id": 1,
                    "rut": "1111111-1",
                    "name": "user",
                    "active": True
                },
            ]
        )
    
    def test_list_rent(self):
        response = self.apiclient.get('/api/rents/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            [
                {
                    "id_client": 1,
                    "id_company": 1,
                    "daily_cost": 1500,
                    "days": 3
                },
            ]
        )
    
    def test_create_company(self):
        data = {
            "id": "2",
            "name": "myCompany2"
        }
        response = self.apiclient.post('/api/companys/', data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(
            Company.objects.filter(
                id=data["id"],
                name=data["name"],
            ).exists()
        )