# Projeto: Análise de Ações com Python

Este repositório apresenta um projeto focado na análise de dados financeiros de ações utilizando a biblioteca **yfinance**. O código-fonte realiza o download de dados históricos, calcula os retornos diários e gera estatísticas importantes. Esta é uma abordagem simples, eficiente e alternativa ao uso de APIs mais complexas.

## Objetivo

O objetivo é introduzir o uso de bibliotecas Python como **yfinance** para coleta e análise de dados financeiros, permitindo que os usuários executem tarefas como:

- Baixar dados históricos de ações.
- Calcular estatísticas financeiras, como retornos diários médios.
- Exportar os dados processados para um arquivo CSV.

## Estrutura do Projeto

- **/src**: Contém o código principal em Python.
- **/data**: Repositório para arquivos de saída como os CSVs gerados.
- **/docs**: Notas e explicações adicionais sobre o projeto.

## Tecnologias Utilizadas

- **Python**
- **yfinance**: Biblioteca para acesso fácil a dados financeiros.
- **pandas**: Para manipulação de dados.

## Requisitos

Certifique-se de ter instalado os seguintes pacotes antes de executar o código:

```bash
pip install yfinance pandas
```

## Como Executar

1. Clone este repositório:

```bash
git clone https://github.com/seuusuario/seurepositorio.git
```

2. Navegue até o diretório do projeto:

```bash
cd seurepositorio
```

3. Execute o script Python:

```bash
python src/analise_acoes.py
```

## Funcionalidades

1. **Baixar Dados**:
   O script utiliza a função `yf.download` para buscar dados históricos do ticker configurado (ex.: `AAPL`).

2. **Análise de Retornos**:
   - Calcula o retorno diário da ação.
   - Gera métricas como média, máximo e mínimo dos retornos diários.

3. **Exporta para CSV**:
   - Salva os dados históricos e as estatísticas geradas em um arquivo `daily_stock_prices.csv`.

## Saída do Programa

A saída inclui:

- Retorno diário médio.
- Retorno diário máximo.
- Retorno diário mínimo.
- Um arquivo CSV com os dados históricos e os cálculos adicionais.

## Exemplos de Resultados

```plaintext
Average Daily Return: 0.0012
Maximum Daily Return: 0.045
Minimum Daily Return: -0.038
```

## Contribuições

São bem-vindas contribuições para:

- Melhorar a análise estatística.
- Adicionar novas funcionalidades, como visualização de dados.

## Licença

Este projeto está sob a licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.

---

**Nota:** Este projeto reflete a evolução do aprendizado em Python, e futuras iterações incluirão funcionalidades mais avançadas.
