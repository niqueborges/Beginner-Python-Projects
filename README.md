# Projeto: Aumentando a Produtividade com Python

Este repositório faz parte de uma série de projetos dedicados ao aumento da produtividade no uso de Python. O foco principal deste primeiro projeto é demonstrar como acessar e analisar dados financeiros utilizando a biblioteca `yfinance` e realizar tarefas comuns de análise de dados, como cálculos estatísticos e exportação de dados para arquivos CSV.

## Objetivo
Este projeto tem como objetivo:
- Facilitar o acesso a dados financeiros de ações usando APIs públicas.
- Demonstrar como usar ferramentas como `pandas` e `yfinance` para manipular dados.
- Introduzir boas práticas de programação e testes automatizados com `unittest`.

## Estrutura do Repositório
- **``**: Contém o código principal para baixar, processar e analisar os dados financeiros.
- **`test`**: Contém os testes automatizados para validar as funcionalidades do projeto.
- **`requirements.txt`**: Lista das dependências do projeto.
- **`README.md`**: Este arquivo, com informações gerais sobre o projeto.

## Tecnologias Utilizadas
- **Python**: Linguagem principal para o desenvolvimento do projeto.
- **yfinance**: Biblioteca para acessar dados financeiros de forma simples.
- **pandas**: Para manipulação e análise de dados.
- **unittest**: Para testes automatizados.

## Pré-requisitos
Certifique-se de ter o Python 3.7 ou superior instalado. Em seguida, instale as dependências executando:

```bash
pip install -r requirements.txt
```

## Como Executar o Projeto
1. Execute o arquivo principal para analisar os dados de uma ação específica e salvar o relatório:

   ```bash
   python main.py
   ```

2. Para rodar os testes automatizados e garantir que o projeto está funcionando corretamente:

   ```bash
   python -m unittest test_stock_analysis.py
   ```

## Próximos Projetos
Este é o primeiro de uma série de projetos que visam aumentar a produtividade no uso de Python. Projetos futuros incluirão:
- Automação de tarefas repetitivas com Python.
- Análise avançada de dados com `pandas` e `numpy`.
- Integração com APIs para coleta de dados em tempo real.
- Desenvolvimento de dashboards interativos com `Streamlit`.

## Contribuições
Contribuições são bem-vindas! Se você deseja adicionar novas funcionalidades, corrigir bugs ou melhorar a documentação, fique à vontade para abrir um pull request.

## Licença
Este projeto está licenciado sob a licença MIT. Consulte o arquivo `LICENSE` para obter mais informações.

---

Aumente sua produtividade com Python e fique atento para os próximos projetos desta série! 🚀
