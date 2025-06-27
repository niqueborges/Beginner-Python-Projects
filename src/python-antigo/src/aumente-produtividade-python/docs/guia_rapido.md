# Guia Rápido de Uso

Este guia apresenta uma visão geral sobre como configurar e utilizar os scripts do repositório **Aumente sua Produtividade com Python**. Siga as etapas abaixo para começar!

---

## 🎯 Objetivo

Automatizar tarefas e aumentar a produtividade com 20 scripts Python organizados em categorias como:
- Automação
- Análise de Dados
- Web Scraping
- Gerenciamento de Arquivos
- Conversores e outros

---

## 🚀 Passo a Passo para Configuração

### 1. Clone o Repositório
Abra o terminal e execute o comando:

```bash
git clone https://github.com/seuusuario/aumente-produtividade-python.git
cd aumente-produtividade-python
```

### 2. Crie e Ative um Ambiente Virtual
Crie um ambiente virtual para isolar as dependências do projeto:

```bash
python -m venv venv
```

Ative o ambiente virtual:
- **Linux/Mac**:
  ```bash
  source venv/bin/activate
  ```
- **Windows**:
  ```bash
  venv\Scripts\activate
  ```

### 3. Instale as Dependências

Com o ambiente virtual ativado, instale as dependências necessárias:

```bash
pip install -r requirements.txt
```

---

## 📂 Estrutura de Diretórios

O repositório segue a seguinte organização:

```plaintext
scripts/                     # Scripts principais organizados por categoria
├── automacao/               # Automação de tarefas
├── analise_dados/           # Análise e manipulação de dados
├── web_scraping/            # Extração de dados da web
├── gerenciamento_arquivos/  # Organização e manipulação de arquivos
├── conversores/             # Conversores de formatos
└── diversos/                # Scripts adicionais úteis

tests/                       # Testes unitários e de integração para os scripts
├── automacao/
├── analise_dados/
├── web_scraping/
├── gerenciamento_arquivos/
└── diversos/

docs/                        # Documentação adicional
├── guia_rapido.md           # Este guia rápido
└── contribuicao.md          # Informações para contribuir com o projeto
```

---

## 🛠 Como Executar os Scripts

1. Navegue até a pasta do script desejado, por exemplo:
   ```bash
   cd scripts/automacao
   ```

2. Leia o README da pasta para entender os detalhes do script.

3. Execute o script:
   ```bash
   python nome_do_script.py
   ```

---

## 📑 Exemplo de Uso

### Script: Gerador de Relatórios Excel

1. Navegue para a pasta do script:
   ```bash
   cd scripts/analise_dados
   ```

2. Execute o script:
   ```bash
   python gerador_relatorios.py
   ```

3. Verifique o arquivo gerado na pasta `output/`.

---

## ⚙️ Requisitos do Sistema

- Python 3.7 ou superior
- Pip (gerenciador de pacotes)
- Dependências listadas em `requirements.txt`

---

## 💡 Dicas

- Use `pytest` para rodar os testes unitários e garantir que os scripts funcionam como esperado:
  ```bash
  pytest
  ```

- Consulte a documentação específica de cada script para personalizar entradas e saídas.

🎉
