# Emprestimos Bancários

Esse é um projeto web que gerencia propostas de empréstimos. Ele consiste em um backend desenvolvido com Django e Django Rest Framework, um frontend desenvolvido com Vue.js.

A biblioteca RabbitMQ é utilizada como um sistema de mensageria para o processamento assíncrono das propostas de empréstimo, quando uma nova proposta de empréstimo é cadastrada, ela é enviada para uma fila de processamento no RabbitMQ. O Celery, uma biblioteca de tarefas distribuídas, é responsável por consumir as mensagens da fila e realizar o processamento assíncrono das propostas. O resultado do processamento de uma proposta de empréstimo pode alterar o seu status. Após o processamento, o status da proposta é atualizado e refletido na interface do usuário.

Através da integração de diferentes tecnologias e o uso de processamento assíncrono, o projeto proporciona uma experiência de usuário ágil, com atualizações em tempo real e um desempenho otimizado.

## Requisitos

Certifique-se de ter os seguintes requisitos instalados em sua máquina:

- Docker
- Git

## Como executar o projeto

Siga as etapas abaixo para executar o projeto localmente:

1. Clone o repositório:
   ```shell
   git clone https://github.com/zeguil/Desafio-DigitalSysTec.git
2. Navegue até o diretório do projeto:
    ```shell
    cd Desafio-DigitalSysTec
3. Inicie o ambiente Docker:
    ```shell
    docker-compose up --build
Esse comando irá construir e iniciar os contêineres Docker para o backend, frontend, RabbitMQ e Celery.

Aguarde até que todos os contêineres sejam iniciados. Após a conclusão, você poderá acessar o aplicativo no navegador.

- Aplicação Django: http://localhost:8000
- Aplicação Vue.js: http://localhost:8080

Para acessar o painel de administração do Django em http://localhost:8000/admin, você pode usar as seguintes credenciais:

- Username: admin
- Senha: psswrd123

Certifique-se de que o ambiente Docker esteja em execução para acessar o Django Admin.
# Encerrando o projeto
Para encerrar o ambiente Docker, você pode pressionar *Ctrl + C* no terminal onde o comando *docker-compose up* foi executado. Isso irá parar todos os serviços.

# Estrutura do Projeto
O projeto é organizado da seguinte maneira:

- O código do backend Django está localizado na pasta backend.
- O código do frontend Vue.js está localizado na pasta frontend.
- O arquivo docker-compose.yml define a configuração do ambiente Docker, incluindo os serviços do backend, frontend, RabbitMQ, Celery e o banco de dados PostgreSQL.

# Observações
- Certifique-se de ter as portas 8000 e 8080 disponíveis em sua máquina para evitar conflitos com outros serviços em execução.
- O banco de dados PostgreSQL está sendo utilizado como o banco de dados padrão para o projeto. Certifique-se de que o ambiente Docker esteja em execução para que o banco de dados seja acessível para a aplicação Django.

## Créditos

- Desenvolvido por [José Guilherme Lins](https://github.com/zeguil)
