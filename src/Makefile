# Diretório do ambiente virtual
VENV_DIR=venv
PYTHON=$(VENV_DIR)/bin/python
PIP=$(VENV_DIR)/bin/pip

# Ambiente: development (padrão) ou production
ENV ?= development
ENV_FILE = .env.$(ENV)

# Caminho do script principal (ajuste conforme seu projeto)
SRC=.python-projects
PYTHON=$(VENV_DIR)/bin/python

# ========== Tarefas ==========

# Cria o ambiente virtual e instala dependências 
setup:
	python3 -m venv $(VENV_DIR)
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

# Ativa o ambiente (só exibe instrução)
activate:
	@echo "Use: source $(VENV_DIR)/bin/activate"

# Instala dependências principais
install:
	$(PIP) install -r requirements.txt

# Executa a aplicação com as variáveis de ambiente corretas
run:
	@echo "Executando em ambiente $(ENV)..."
	@export $(shell cat $(ENV_FILE) | xargs) && $(PYTHON) $(MAIN)

# Formata o código com Black
format:
	$(VENV_DIR)/bin/black .

# Executa testes com pytest
test:
	$(VENV_DIR)/bin/pytest

# Remove arquivos temporários
clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -name "*.pyc" -delete

# Remove o ambiente virtual
reset:
	rm -rf $(VENV_DIR)
