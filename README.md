# django-rest
As imagens do virtual enviorment são maiores que o limite do git e na minha internet vai demorar muito tempo para subir para o google drive. Então:

1 - Criar o virtual enviroment:
cd ~/django-rest/RunningTimeRESTAPI
python3 -m venv env

2 - Ativar a venv 
no windows:
env\Scripts\activate.bat
linux/mac:
source tutorial-env/bin/activate

3 - instalar as requirements 
pip install -r requirements.txt

3.1 - (opcional) configurar o project interpreter no pycharm
em configurações -> project -> project interpreter
add new interpreter (gear icon)
virtualenv environment -> existing environment
em windows:
~/RunningTimeRESPAPI/Scripts/python.exe
em linux/mac
~/RunningTimeRESPAPI/env/bin/python

se tudo der certo é para aparecer os pacotes instalados

Passo 4 e 5 dentro da venv
4 - subir o server
python manage.py runserver

5 - realizar uma chamada
em outra janela do terminal:
cd runningTimeRESTAPI/runningTime
http --json GET http://127.0.0.1:8000/running_time/ < test.json
