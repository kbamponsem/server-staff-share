init:
	pip install -r requirements.txt

format:
	autopep8 --in-place --recursive .

run: 
	gunicorn --bind 0.0.0.0:3000 -w 4  main:app --reload --logger-class _shared.AppLogger