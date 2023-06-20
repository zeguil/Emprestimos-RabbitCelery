from celery import shared_task
from .models import Proposta


@shared_task
def process_proposta(proposta_id):
    proposta = Proposta.objects.get(id=proposta_id)
    
    if proposta.id % 2 == 0:
        proposta.status = 'Aprovada'
    else:
        proposta.status = 'Negada'
    proposta.save()