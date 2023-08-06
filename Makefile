
NAME=ai_assistant
USER=$(shell id -u):$(shell id -g)

clean: clean-build clean-pyc

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr *.egg-info

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

build:
	docker-compose build ai_assistant
	docker-compose build linter

format:
	docker-compose run --rm --user $(USER) linter black src/

bash:
	docker-compose run --rm --user $(USER) ai_assistant bash

# unfurtunatly, port binding is not supported for MAC OS in docker compose, this why we use docker rather than docker compose
run: 
	docker run --rm -it -p 8000:8000 ai_assistant python src/main.py

jupyter:
	docker run --rm -it -p 8888:8888 --user $(USER) ai_assistant jupyter lab notebook/ --ip 0.0.0.0 --allow-root
