HOST=127.0.0.1
pip:=$(shell which pip)
app=staff-share

init:
	$(pip) install virtualenv
	$(python) virtualenv venv
	
install:
	$(pip) install -r requirements.txt

isort:
	sh -c "isort --skip-glob=.tox --recursive . "

format: isort
	autopep8 --in-place --aggressive --recursive _shared features main.py urls.py
	pycodestyle features _shared main.py urls.py 

changelog:
	gitchangelog $(version) > CHANGELOG

commit:
	git add .
	git commit

run: 
	gunicorn -w 4  main:app --logger-class _shared.AppLogger


# DOCKER COMMANDS
logs:
	docker  logs --tail 10 -f ${app}

compose:
	docker-compose up -d


compose-build:
	docker-compose up -d --build

stats:
	docker ps

login:
	docker exec -it ${app} /bin/sh

volumes:
	docker volume ls

stop:
	docker-compose down

connect-db:
	docker exec -it mysql mysql -u root -p idoc_db
