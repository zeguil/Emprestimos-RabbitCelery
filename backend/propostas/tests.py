from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Proposta

class PropostaAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_criar_proposta(self):
        data = {
            'nome_completo': 'João',
            'cpf': '12345678901',
            'endereco': 'Rua Teste, 123',
            'valor_emprestimo': '1000.00'
        }
        response = self.client.post('/propostas/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Proposta.objects.count(), 1)
        self.assertEqual(Proposta.objects.get().nome_completo, 'João')
        self.assertEqual(Proposta.objects.get().cpf, '12345678901')
       

    def test_listar_propostas(self):
        response = self.client.get('/propostas/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        

