SHELL := /bin/bash

.PHONY: all
all: venv


venv: venv/bin/activate

venv/bin/activate: requirements.txt
	python3 -m venv venv
	source venv/bin/activate; pip install -r requirements.txt

.PHONY: freeze
freeze:
	source venv/bin/activate; pip freeze > requirements.txt

.PHONY: clean
clean:
	rm -rf venv
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -delete


http-serve:
	python app.py