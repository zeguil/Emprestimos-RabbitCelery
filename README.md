# Desafio DigitalSysTec

Este é o repositório do Desafio DigitalSysTec, que consiste em um projeto Django com frontend em Vue.js e utiliza RabbitMQ e Celery para processamento assíncrono.

## Requisitos

Certifique-se de ter os seguintes requisitos instalados em sua máquina:

- Docker
- Git

## Como executar o projeto

Siga as etapas abaixo para executar o projeto localmente:

1. Clone o repositório:

   ```shell
   git clone https://github.com/zeguil/Desafio-DigitalSysTec.git
Navegue até o diretório do projeto:

shell
Copy code
cd Desafio-DigitalSysTec
Inicie o ambiente Docker:

shell
Copy code
docker-compose up --build
Esse comando irá construir e iniciar os contêineres Docker para o backend, frontend, RabbitMQ e Celery.

Aguarde até que todos os contêineres sejam iniciados. Após a conclusão, você poderá acessar o aplicativo no navegador.

Aplicação Django: http://localhost:8000
Aplicação Vue.js: http://localhost:8080
Para acessar o painel de administração do Django, você pode usar as seguintes credenciais:

URL do Django Admin: http://localhost:8000/admin
Username: admin
Senha: psswrd123
Certifique-se de que o ambiente Docker esteja em execução para acessar o Django Admin.

Estrutura do Projeto
O projeto é organizado da seguinte maneira:

O código do backend Django está localizado na pasta backend.
O código do frontend Vue.js está localizado na pasta frontend.
O arquivo docker-compose.yml define a configuração do ambiente Docker, incluindo os serviços do backend, frontend, RabbitMQ e Celery.