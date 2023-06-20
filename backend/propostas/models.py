from django.db import models
from django.core.exceptions import ValidationError

class Proposta(models.Model):
    nome_completo = models.CharField(max_length=80)
    cpf = models.CharField(max_length=11, unique=True, error_messages={
        'unique': 'Já existe uma proposta com o mesmo CPF.'
    })
    endereco = models.CharField(max_length=200)
    valor_emprestimo = models.DecimalField(max_digits=10, decimal_places=2, error_messages={
        'max_digits': 'O valor do empréstimo deve ter no máximo 10 dígitos.',
        'decimal_places': 'O valor do empréstimo deve ter no máximo 2 casas decimais.'
    })
    status = models.CharField(max_length=10, choices=[('Aprovada', 'Aprovada'), ('Negada', 'Negada')], default='Aguardando')

    def __str__(self):
        return self.nome_completo
