PYTHON=python
REDIS=redis-server

.PHONY: worker enqueuer redis dashboard

worker:
	$(PYTHON) -m spitter

enqueuer:
	$(PYTHON) -m enqueuer

redis:
	$(REDIS)

dashboard:
	rq-dashboard
