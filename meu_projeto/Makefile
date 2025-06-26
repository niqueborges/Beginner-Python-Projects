# Caminhos e comandos
VENV = .venv
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip

.PHONY: install run clean test lint format build reset freeze

# Instala dependências do requirements.txt
install:
	$(PIP) install -r ../requirements.txt

# Executa o app com variáveis do .env.dev
run:
	ENV_FILE=.env.dev $(PYTHON) app.py

# Limpa arquivos compilados e caches
clean:
	find . -name "*.pyc" -delete
	find . -name "__pycache__" -delete

# Roda testes com unittest (mude para pytest se quiser)
test:
	$(PYTHON) -m unittest discover -s tests

# Verifica estilo de código com flake8
lint:
	$(VENV)/bin/flake8 src tests

# Formata código com black
format:
	$(VENV)/bin/black .

# Gera build (para empacotar seu projeto)
build:
	$(PYTHON) setup.py sdist bdist_wheel

# Remove virtualenv e arquivos de build/cache
reset: clean
	rm -rf $(VENV) dist *.egg-info .pytest_cache .mypy_cache

# Gera ou atualiza requirements.txt com dependências instaladas
freeze:
	$(PIP) freeze > requirements.txt



.PHONY: install run clean






