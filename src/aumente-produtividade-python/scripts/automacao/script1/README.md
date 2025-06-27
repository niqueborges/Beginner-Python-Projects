# Automacao de Relatorio de Vendas com Envio de E-mails

Este projeto automatiza a geração de relatórios de vendas a partir de um arquivo CSV e o envio desses relatórios por e-mail. Inicialmente, o envio de e-mails foi implementado utilizando a biblioteca `win32com.client` para integrar com o Microsoft Outlook. Devido a limitações técnicas e problemas de compatibilidade, a abordagem foi alterada para usar o protocolo SMTP com a biblioteca `smtplib`.

## Índice

1. [Visão Geral do Projeto](#visão-geral-do-projeto)
2. [Requisitos](#requisitos)
3. [Configuração do Ambiente](#configuração-do-ambiente)
4. [Mudanças no Código](#mudanças-no-código)
5. [Como Executar](#como-executar)
6. [Próximos Passos](#próximos-passos)

---

## Visão Geral do Projeto

O projeto:

- Lê dados de vendas de um arquivo CSV.
- Calcula valores como total, média, máximo e mínimo das vendas.
- Gera um relatório formatado com os dados processados.
- Envia o relatório como corpo de um e-mail com o arquivo CSV anexado.

Inicialmente, a integração foi feita com o Microsoft Outlook via `win32com.client`, mas problemas relacionados ao uso da versão da Microsoft Store impediram o envio de e-mails. A solução alternativa utiliza SMTP, o que amplia a compatibilidade e independência da aplicação.

---

## Requisitos

- Python 3.8 ou superior
- Bibliotecas Python:
  - `pandas`
  - `python-dotenv`
  - `smtplib` (embutido no Python)
- Conta de e-mail configurada para envio via SMTP

---

## Configuração do Ambiente

1. **Instale as dependências:**
   ```bash
   pip install pandas python-dotenv
   ```

2. **Configure o arquivo `.env`:**
   Crie um arquivo `.env` no diretório raiz do projeto com as seguintes variáveis:
   ```env
   SENDER_EMAIL=seu_email@gmail.com
   SENDER_PASSWORD=sua_senha
   RECIPIENT_EMAIL=email_destinatario@gmail.com
   ```

   - Substitua `seu_email@gmail.com` pelo seu e-mail.
   - Substitua `sua_senha` pela senha ou senha de app (para Gmail com 2FA).
   - Substitua `email_destinatario@gmail.com` pelo e-mail do destinatário.

3. **(Opcional) Configurações do provedor SMTP:**
   Caso use outro provedor de e-mail, ajuste os parâmetros no código para o servidor SMTP e porta correspondentes.

---

## Mudanças no Código

### Problema Inicial

O uso de `win32com.client` para integrar com o Microsoft Outlook apresentou as seguintes dificuldades:
- O aplicativo Outlook da Microsoft Store não suporta automação via COM.
- Dependência de uma configuração específica no Windows, limitando a portabilidade.

### Solução Implementada

Optamos por usar o protocolo SMTP com a biblioteca `smtplib`, uma solução mais portável e independente. Isso permite o envio de e-mails através de diferentes provedores, como Gmail, Outlook e Yahoo.

### Principais Mudanças:

1. Substituímos a função `send_email` por uma implementação baseada em `smtplib`.
2. Adicionamos suporte para anexos usando `email.mime`.
3. Incluímos o uso de variáveis de ambiente para proteger credenciais de e-mail.

### Benefícios:

- Maior compatibilidade entre provedores de e-mail.
- Redução de dependências externas.
- Melhoria na segurança ao evitar credenciais expostas diretamente no código.

---

## Como Executar

1. **Prepare o CSV:**
   Certifique-se de que o arquivo `sales.csv` esteja no diretório especificado com o seguinte formato:
   ```csv
   sales
   100
   200
   150
   ```

2. **Execute o script:**
   ```bash
   python script.py
   ```

3. **Resultado:**
   - O relatório será enviado para o destinatário configurado.
   - O arquivo `sales.csv` será anexado ao e-mail.

---

## Próximos Passos

- Adicionar suporte para envio a múltiplos destinatários.
- Implementar logs para monitorar os envios de e-mails.
- Criar uma interface gráfica para facilitar a configuração e execução do script.

---

## Autor

Este projeto foi desenvolvido como uma solução para problemas práticos de automação com Python. Sinta-se à vontade para contribuir ou sugerir melhorias.