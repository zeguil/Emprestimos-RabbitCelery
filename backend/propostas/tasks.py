from celery import shared_task
from .models import Proposta

def aprovar_proposta(proposta):
    return proposta.id % 2 == 0 

@shared_task
def processar_proposta(proposta_id):
    proposta = Proposta.objects.get(id=proposta_id)
    if aprovar_proposta(proposta):
        proposta.status = 'Aprovada'
    else:
        proposta.status = 'Negada'
    proposta.save()