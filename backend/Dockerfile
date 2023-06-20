FROM python:3.10

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

RUN python manage.py makemigrations

ENV DJANGO_SETTINGS_MODULE=propostas_emprestimo.settings

CMD python manage.py collectstatic --no-input
