FROM python:3.10

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

ENV DJANGO_SETTINGS_MODULE=propostas_emprestimo.settings

CMD python manage.py collectstatic --no-input && python manage.py runserver 0.0.0.0:8000
