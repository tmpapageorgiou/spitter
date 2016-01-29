PYTHON=python
REDIS=redis-server

.PHONY: run start-redis dashboard

worker:
	$(PYTHON) -m spitter

redis:
	$(REDIS)

dashboard:
	rq-dashboard

enqueuer:
	$(PYTHON) loader.py
