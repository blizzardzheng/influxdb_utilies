VIRTUALENV = $(shell which virtualenv)

clean: kill
	rm -fr venv

venv:
	$(VIRTUALENV) venv

install: venv
	. venv/bin/activate; pip install -r requirements.txt

start: venv install
	docker-compose up -d

convert: venv
	. venv/bin/activate; python convert_csv.py

stop:
	docker-compose stop

kill: stop
	docker-compose rm
