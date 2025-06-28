# Detecta o ambiente virtual que está ATIVO no seu terminal.
# Se nenhum estiver ativo, ele usa o 'python3' do sistema (o que causa o erro).
PYTHON := $(or $(wildcard $(VIRTUAL_ENV)/bin/python),python3)

# Define o nome do arquivo de dependências (agora na mesma pasta)
REQUIREMENTS_FILE = requirements.txt

# --- Comandos do Projeto ---

.PHONY: help install run-dev run-prod clean

# Comando 'help' para exibir a ajuda
help:
	@echo "Comandos disponíveis:"
	@echo "  make install    -> Instala as dependências de $(REQUIREMENTS_FILE)"
	@echo "  make run-dev    -> Executa a aplicação em ambiente de desenvolvimento"
	@echo "  make clean      -> Remove arquivos temporários do Python"

# Comando 'install' para instalar dependências
install:
	@echo "Usando o Python em: $(PYTHON)"
	@echo "Instalando dependências de $(REQUIREMENTS_FILE)..."
	$(PYTHON) -m pip install -r $(REQUIREMENTS_FILE)

# Comando 'run-dev' para executar em modo de desenvolvimento
run-dev:
	@echo "Iniciando a aplicação em modo de Desenvolvimento..."
	export FLASK_ENV=development && \
	export ENV_FILE=.env.dev && \
	$(PYTHON) app.py

# Comando 'clean' para limpar o projeto
clean:
	@echo "Limpando arquivos temporários..."
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete