HOST=127.0.0.1
PORT=3000

init:
	pip install -r requirements.txt

isort:
	sh -c "isort --skip-glob=.tox --recursive . "

format: isort
	autopep8 --in-place --recursive .

run: 
	gunicorn --bind $(HOST):$(PORT) -w 4  main:app --reload --logger-class _shared.AppLogger