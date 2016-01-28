PYTHON=python
REDIS=redis-server

.PHONY: run

run:
	$(PYTHON) -m spitter

start-redis:
	$(REDIS)
