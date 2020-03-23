# django-rest
Serviço django-rest para o cálculo do running-time
## Subir o servidor dentro de uma venv:
1. **Criar o virtual enviroment:**<br/>
	1. cd ~/django-rest/RunningTimeRESTAPI
	2. python3 -m venv env
2.  **Ativar a venv:**<br/>
	* no windows:
		env\Scripts\activate.bat
	* linux/mac:
		source env/bin/activate
3. **Instalar as requirements:**<br/>
	pip install -r requirements.txt
 > **(opcional) configurar o project interpreter no pycharm:**
> 1. Em configurações -> project -> project interpreter
> 2. Add new interpreter (gear icon)
> 3. Virtualenv environment -> existing environment
>    * em windows:
> ~/RunningTimeRESPAPI/Scripts/python.exe
>    * em linux/mac:
> ~/RunningTimeRESPAPI/env/bin/python
> 
>Se tudo der certo é para aparecer os pacotes instalados

**Passo 4 e 5 dentro da venv:**

4. **Subir o server:**<br/>
python manage.py runserver
5. **Realizar uma chamada:**<br/>
Em outra janela do terminal:
	1. cd runningTimeRESTAPI/runningTime
	2. http --json GET http://127.0.0.1:8000/running_time/ < test.json
## Subir o servidor utilizando o Docker:
1. **Build docker image:**<br/>
	docker build -t runningTimeDocker -f Dockerfile
2. **Run container:**<br/>
	docker run -it -p 8888:8888 runningTimeDocker
3. **Realizar uma chamada:**<br/>
	Em outra janela do terminal: numa venv com httpie instalada, pode ser a venv da parte anterior:<br/>
	http -format -JSON GET http://0.0.0.0:8888/runningtime/ < ~/successful_test.json
