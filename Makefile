.PHONY: build
build: .venv graphabc/* setup.py version.py README.md
	. ./.venv/bin/activate
	python setup.py sdist bdist_wheel

.PHONY: upload
upload: build
	twine upload --config-file .pypirc dist/*

.PHONY: docker
docker:
	xhost +local:
	docker build --no-cache -t graphabc-test-env .
	docker run -v ./graphabc:/build/graphabc -v $(HOME)/.Xauthority:/home/nonroot/.Xauthority -e DISPLAY=$(DISPLAY) --pid=host -v /tmp/.X11-unix:/tmp/.X11-unix:ro -it graphabc-test-env bash

.venv:
	python -m venv .venv
	pip install --upgrade pip
	pip install setuptools
	pip install raylib

.PHONY: clean
clean:
	[ -e .eggs ] && rm -rf .eggs/ || :
	[ -e __pycache__ ] && rm -rf __pycache__ || :
	find graphabc -depth -name __pycache__ -exec rm -r '{}' ';'
	find test -depth -name __pycache__ -exec rm -r '{}' ';'
	[ -e build ] && rm -rf build || :
	[ -e dist ] && rm -rf dist || :
	[ -e graphabc.egg-info ] && rm -rf graphabc.egg-info || :

.PHONY: listfns
listfns:
	truncate -s 0 funcs-my.lst
	rg -IN '^\s*def\s*[^\s_]' graphabc/shapes.py >> funcs-my.lst && echo >> funcs-my.lst
	rg -IN '^\s*def\s*[^\s_]' graphabc/colors.py >> funcs-my.lst && echo >> funcs-my.lst
	rg -IN '^\s*def\s*[^\s_]' graphabc/pen.py >> funcs-my.lst && echo >> funcs-my.lst
	rg -IN '^\s*def\s*[^\s_]' graphabc/brush.py >> funcs-my.lst && echo >> funcs-my.lst
	rg -IN '^\s*def\s*[^\s_]' graphabc/text.py >> funcs-my.lst && echo >> funcs-my.lst
	rg -IN '^\s*def\s*[^\s_]' graphabc/picture.py >> funcs-my.lst && echo >> funcs-my.lst
	rg -IN '^\s*def\s*[^\s_]' graphabc/window.py >> funcs-my.lst && echo >> funcs-my.lst
	rg -IN '^\s*def\s*[^\s_]' graphabc/events.py >> funcs-my.lst && echo >> funcs-my.lst
	#rg -Hn -g '!main.py' -g '!render_funnel*.py' -g '!event_loop.py' -g '!context.py' -g '!mouse_h.py' --sort=path graphabc/ > funcs-my.lst
