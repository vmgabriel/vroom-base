ENV=development


all: clean install load
dev: test lint

test:
	python -m pytest tests/ -v


lint:
	flake8 --exclude=venv


run:
	python3 manage.py


load:
	bash -c "source venv/bin/activate"


clean:
	rm -rf venv
	rm -Rf .pytest_cache
	rm -Rf __pycache__
	rm -Rf */*/__pycache__
	find tests -type f -name "*-test.json" -delete
	find . -type f -name "*.pyc" -delete


install-dev:
	docker-compose -f compose/local.yml build
	python -m virtualenv venv
	chmod +x venv/bin/activate
	make load && ./venv/bin/pip install -r requirements/development.txt


install-prod:
	docker-compose -f compose/local.yml build
	pip install -r requirements/production.txt


install:
ifeq ($(ENV), development)
	make install-dev
endif
ifeq ($(ENV), production)
	make install-prod
endif
ifeq ($(ENV), undefined)
	make install-dev
endif
