SHELL := /bin/bash
.PHONY: help init publish docs

help:
	@echo "init     - install requirements"
	@echo "publish  - publish to pypi"
	@echo "docs     - generate html docs"

init:
	pip3 install -r requirements.txt

publish:
	python3 setup.py register
	python3 setup.py sdist upload

docs:
	@cd docs && make html
