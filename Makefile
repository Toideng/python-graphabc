.PHONY: build
build: .venv graphabc/* setup.py version.py README.md
	. ./.venv/bin/activate
	python setup.py sdist bdist_wheel

.PHONY: upload
upload: build
	twine upload --config-file .pypirc dist/*

docker:
	xhost +local:
	docker build --no-cache -t graphabc-test-env .
	docker run -v ./graphabc:/build/graphabc -v $(HOME)/.Xauthority:/home/nonroot/.Xauthority -e DISPLAY=$(DISPLAY) --pid=host -v /tmp/.X11-unix:/tmp/.X11-unix:ro -it graphabc-test-env bash

.venv:
	python -m venv .venv
	pip install --upgrade pip
	pip install setuptools
	pip install raylib

clean:
	[ -e .eggs ] && rm -rf .eggs/ || :
	[ -e __pycache__ ] && rm -rf __pycache__ || :
	find graphabc -depth -name __pycache__ -exec rm -r '{}' ';'
	find test -depth -name __pycache__ -exec rm -r '{}' ';'
	[ -e build ] && rm -rf build || :
	[ -e dist ] && rm -rf dist || :
	[ -e graphabc.egg-info ] && rm -rf graphabc.egg-info || :
