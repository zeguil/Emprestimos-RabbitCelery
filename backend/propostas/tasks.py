from celery import shared_task
from .models import Proposta
from django.core.exceptions import ObjectDoesNotExist
import logging
logger = logging.getLogger(__name__)

@shared_task
def processar_proposta(proposta_id):
    try:
        proposta = Proposta.objects.get(id=proposta_id)
        if proposta.id % 2 == 0:
            proposta.status = 'Aprovada'
        else:
            proposta.status = 'Negada'
        proposta.save()
    except ObjectDoesNotExist:
        logger.error(f"A proposta com ID {proposta_id} não foi encontrada.")
        pass
