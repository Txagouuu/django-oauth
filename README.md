# 🌌 Django oAuth 2.0

Este repositório contém o código-fonte do projeto **ADjango oAuth 2.0**, uma galeria de imagens do espaço, desenvolvido durante o curso de **Formação Django** da [Alura](https://www.alura.com.br/). O objetivo principal deste projeto é aplicar os conceitos fundamentais do framework Django para construir uma aplicação web funcional utilizado a biblioteca django-allauth para a utilização de oAuth 2.0.

> 🚀 **Status:** Concluído

##  functionalities

* [X] Sistema de usuários e autenticação .

## 🛠️ Tecnologias Utilizadas

* **Backend:** Python, Django
* **Frontend:** HTML, CSS
* **Banco de Dados:** SQLite3 (para desenvolvimento)
* **Gerenciamento de Pacotes:** Pip

## ⚙️ Como Rodar o Projeto Localmente

Siga os passos abaixo para configurar e executar o projeto em sua máquina.

**Pré-requisitos:**
* Python 3.8+
* Git

**Passos:**

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/Txagouuu/django-oauth.git
    cd django-oauth
    ```

2.  **Crie e ative um ambiente virtual:**
    ```bash
    # Criar o ambiente virtual
    python -m venv venv

    # Ativar no Windows
    .\venv\Scripts\activate

    # Ativar no Linux/macOS
    source venv/bin/activate
    ```

3.  **Instale as dependências:**
    O arquivo `requirements.txt` contém todas as bibliotecas Python necessárias.
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure as variáveis de ambiente:**
    Crie um arquivo chamado `.env` na raiz do projeto, copie o conteúdo abaixo e cole nele.
    ```env
    SECRET_KEY='sua-chave-secreta-aqui'
    DEBUG=True
    ```
    > **Dica:** Você pode gerar uma nova `SECRET_KEY` usando o próprio Django. Abra um terminal Python (`python`) e execute:
    > `python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'`

5.  **Aplique as migrações do banco de dados:**
    Este comando irá criar o arquivo `db.sqlite3` e as tabelas necessárias.
    ```bash
    python manage.py migrate
    ```

6.  **Crie um superusuário:**
    Você precisará de um usuário administrador para acessar o painel `/admin/`.
    ```bash
    python manage.py createsuperuser
    ```
    (Siga as instruções para definir nome de usuário, email e senha).

7.  **Execute o servidor de desenvolvimento:**
    ```bash
    python manage.py runserver
    ```

8.  Abra seu navegador e acesse [http://127.0.0.1:8000/](http://127.0.0.1:8000/) para ver o projeto em ação!

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
