# BR MED - Teste

*versao usada no desenvolvimento: python 3.9.0*

## Pré-requisitos

* python 3+
* docker e docker-compose

## Virtual Enviroment

Primeiro preencha as váriaveis no `.env.example` e retire o **.example** do arquivo para criar um `.env`. Depois:

    #Crie e ative o virtual env
    python -m venv venv
    source venv/bin/activate
    
    #Instalando dependencias
    pip install -r requirements.txt

## Iniciando o projeto

Primeiro inicie o `docker-compose.yml`:

    docker-compose up # -d para rodar em segundo plano

Agora, inicie o projeto django:
    
    python manage.py runserver
