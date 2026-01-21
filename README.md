# 🔐 Django OAuth 2.0 Authentication com Allauth

Este repositório documenta meus estudos práticos sobre **autenticação OAuth 2.0 em aplicações Django**, utilizando a biblioteca **django-allauth** para integração com provedores externos como Google, GitHub e outros.

O objetivo é entender não apenas a implementação, mas também os **fluxos de segurança envolvidos**, boas práticas e riscos comuns em sistemas de autenticação modernos.

📚 **Estudo realizado através da plataforma Alura.**

---

## 🎯 Objetivos

* Implementar login social via OAuth 2.0
* Compreender os fluxos:

  * Authorization Code
  * Refresh Token
* Integrar autenticação segura ao Django
---

## 🧰 Tecnologias

* Python 3.11+
* Django 5+
* django-allauth
* SQLite (ambiente de desenvolvimento)
* Provedores OAuth 2.0 (GitHub)

---

## ⚙️ Instalação

```bash
git clone https://github.com/Txagouuu/django-oauth.git
cd django-oauth
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

---

## 🔐 Configuração do Allauth

1. Instalação da biblioteca:

```bash
pip install django-allauth
```

2. Adicione ao `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.github',
]
```

3. Configurações básicas:

```python
SITE_ID = 1
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/accounts/login/'
```

4. Aplicar migrações:

```bash
python manage.py migrate
```

---

## 🛡️ Boas Práticas de Segurança
**Configure as variáveis de ambiente:**
Crie um arquivo chamado `.env` na raiz do projeto, copie o conteúdo abaixo e cole nele.
Inclua no arquivo `.env` os seguintes parâmetros `client_id` e `secret` para questão de uma maior segurança da aplicação

```env
SECRET_KEY='sua-chave-secreta-aqui'
DEBUG=True
```
```env
CLIENT_ID = 'client_id'
SECRET = 'secret'
```
> **Dica:** Você pode gerar uma nova `SECRET_KEY` usando o próprio Django. Abra um terminal Python (`python`) e execute:
> `python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'`

---

## 📚 Referências

* Django Allauth Documentation
* Alura

---

## 👨‍💻 Autor

**Tiago Mendonça**

Software Engineer Student | Cybersecurity Student

Backend • DevSecOps • Security Engineering
