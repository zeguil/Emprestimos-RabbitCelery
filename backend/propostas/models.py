from django.db import models

class Proposta(models.Model):
    nome_completo = models.CharField(max_length=80)
    cpf = models.CharField(max_length=11)
    endereco = models.CharField(max_length=200)
    valor_emprestimo = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, choices=[('Aprovada', 'Aprovada'), ('Negada', 'Negada')], default='Aguardando')
    
    def __str__(self):
        return self.nome_completo
