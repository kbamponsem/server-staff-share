HOST=127.0.0.1
PORT=3000
pip=pip3


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

git-commit: format
	git add .
	git commit

run: 
	# gunicorn --bind $(HOST):$(PORT) -w 4  main:app --reload --logger-class _shared.AppLogger
	python main.py
