# Sistema de Gerenciamento de Viagens

Este projeto é um sistema de gerenciamento de viagens desenvolvido durante o intensivão de 3 aulas da Rocketseat. Ele permite aos usuários planejar e gerenciar todos os aspectos de suas viagens em um único lugar, desde a criação de viagens até a confirmação de participantes.

## Tecnologias Utilizadas

- **Backend:** Python com Flask
- **Banco de Dados:** SQL
- **Outras Ferramentas:** Autenticação, conexão com banco de dados, envio de e-mails

## Funcionalidades

- **Criação de Viagens:** Permite aos usuários criar uma nova viagem.
- **Gerenciamento de Participantes:** Inclui funcionalidades para adicionar participantes às viagens e confirmar sua participação.
- **Envio de Convites por E-mail:** Envio automático de convites para os participantes.
- **Criação e Gerenciamento de Atividades:** Permite aos usuários criar e gerenciar atividades para cada viagem.
- **Criação e Uso de Links para Viagens:** Geração de links únicos para cada viagem, facilitando o compartilhamento.

## Como Executar

1. Clone o repositório:
    ```
    git clone https://github.com/MyTruQs/nlw-journey-python.git
    ```
2. Instale as dependências:
    ```
    pip install -r requirements.txt
    ```

3. Configure o banco de dados SQL conforme necessário.

4. Execute o aplicativo:
    ```
    python run.py
    ```


## Estrutura do Projeto

- `src/controllers`: Contém os controladores para manipulação de lógicas específicas, como criação de viagens e participantes.
- `src/models`: Inclui os modelos e repositórios para interação com o banco de dados.
- `src/models/settings`: Configurações do projeto, incluindo a conexão com o banco de dados.
- `src/routes`: Definições de rotas para a API.

## Contribuições

Contribuições são sempre bem-vindas! Para contribuir, por favor, crie um fork do repositório, faça suas alterações e envie um Pull Request.
