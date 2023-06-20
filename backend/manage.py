import os
import sys
import celery

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'propostas_emprestimo.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # Verifica se o comando 'worker' está presente nos argumentos
    if 'worker' in sys.argv:
        os.environ.setdefault('CELERY_CONFIG_MODULE', 'propostas_emprestimo.celeryconfig')
        # Configura o Celery usando as configurações do Django
        celery.setup_app()

    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
