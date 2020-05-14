HOST=127.0.0.1
PORT=3000

install:
	pip3 install -r requirements.txt

isort:
	sh -c "isort --skip-glob=.tox --recursive . "

format: isort
	autopep8 --in-place --recursive .
	pycodestyle features _shared 

changelog:
	gitchangelog $(version) > CHANGELOG

run: 
	gunicorn --bind $(HOST):$(PORT) -w 4  main:app --reload --logger-class _shared.AppLogger
