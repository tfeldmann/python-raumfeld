init:
	pip3 install -r requirements.txt

publish:
	python3 setup.py register
	python3 setup.py sdist upload
