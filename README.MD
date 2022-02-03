ProjectAgenda
Python 3.9.7

Ambiente de desenvolvimento Linux
#Criar ambiente virtual Python a partir da raiz do projeto
python -m venv venv

#Com ambiente virtual ativado, instalar dependências:
pip install -r requirements.txt

#Rodando aplicação:
python manage.py runserver
Dependências
Sempre que instalar uma nova depencência lembre de atualizar o arquivo requirements.txt

#A partir do ambiente virtual:
pip freeze > requirements.txt