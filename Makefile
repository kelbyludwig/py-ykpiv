.PHONY: build clean test format

all: build

clean:
	rm -f _ykpiv_cffi.*

build:
	pipenv run python ykpiv_build.py

format:
	pipenv run black ykpiv.py ykpiv_build.py

test:
	pipenv run python ykpiv.py
