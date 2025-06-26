VENV = .venv
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip

.PHONY: install run clean

install:
	$(PIP) install -r ../requirements.txt


run:
	ENV_FILE=.env.dev $(PYTHON) app.py

clean:
	find . -name "*.pyc" -delete
	find . -name "__pycache__" -delete

