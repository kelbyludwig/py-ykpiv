.PHONY: build clean test

all: build

clean:
	rm -f _ykpiv_cffi.*

build:
	pipenv run python ykpiv_build.py

test:
	pipenv run python ykpiv.py
