PYTHON=python
REDIS=redis-server

.PHONY: run start-redis dashboard

run:
	$(PYTHON) -m spitter

redis:
	$(REDIS)

dashboard:
	rq-dashboard
