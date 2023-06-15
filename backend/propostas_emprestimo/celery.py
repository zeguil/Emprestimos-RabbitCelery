import os
from celery import Celery

# nome do projeto
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'propostas_emprestimo.settings')

# instância do Celery
app = Celery('propostas_emprestimo')

# configurações para o Celery
app.config_from_object('django.conf:settings', namespace='CELERY')

# registra as tarefas do Celery dentro do projeto 
app.autodiscover_tasks()
