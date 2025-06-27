# Guia de Contribuição

Obrigado por considerar contribuir com o projeto **Aumente sua Produtividade com Python**! Este guia ajudará você a entender como contribuir de forma eficiente, garantindo que o projeto continue organizado e útil para todos.

---

## 📝 Requisitos para Contribuir

Antes de começar, certifique-se de ter o seguinte:

1. **Python** instalado (versão 3.7 ou superior).
2. Um ambiente virtual configurado para isolar as dependências do projeto.
3. Familiaridade com ferramentas Git e GitHub.

---

## 📂 Estrutura do Projeto

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
docs/                        # Documentação adicional
```

---

## 🚀 Como Contribuir

### 1. Faça um Fork do Repositório

1. Clique no botão **Fork** na página principal do repositório.
2. Clone o repositório para o seu ambiente local:
   ```bash
   git clone https://github.com/seuusuario/aumente-produtividade-python.git
   cd aumente-produtividade-python
   ```

### 2. Crie uma Branch

Crie uma branch para a sua feature ou correção:

```bash
git checkout -b minha-nova-feature
```

Nomeie as branches de forma descritiva, por exemplo:
- `fix-bug-envio-email`
- `feature-gerador-relatorios`

### 3. Desenvolva sua Contribuição

- Adicione seus scripts ou melhorias no diretório correspondente em `scripts/`.
- Crie testes para validar seu código em `tests/`.
- Siga as boas práticas da PEP 8.

### 4. Execute os Testes

Certifique-se de que tudo está funcionando antes de enviar sua contribuição:

```bash
pytest
```

### 5. Commit e Push

Faça o commit de suas alterações:

```bash
git add .
git commit -m "Descrição clara da alteração"
```

Envie a branch para o seu fork:

```bash
git push origin minha-nova-feature
```

### 6. Abra um Pull Request

1. Vá até a página principal do repositório original.
2. Clique em **New Pull Request**.
3. Compare sua branch com a branch `main` do repositório original.
4. Adicione uma descrição clara e detalhada do que você alterou.

---

## 🛠 Boas Práticas

- **Escreva Código Limpo**:
  - Use nomes de variáveis e funções descritivos.
  - Adicione comentários para explicar lógicas complexas.

- **Siga a PEP 8**:
  - Utilize ferramentas como `flake8` ou `black` para formatar seu código automaticamente.

- **Teste o Seu Código**:
  - Crie testes unitários para validar suas alterações.
  - Certifique-se de que os testes existentes continuam funcionando.

- **Atualize a Documentação**:
  - Atualize os arquivos em `docs/` para refletir suas alterações, se necessário.

---

## 🎉 Contribuições Aceitas

Estamos abertos a contribuições que:

1. Corrijam bugs.
2. Adicionem novas funcionalidades úteis.
3. Melhorem a performance ou a organização do código.
4. Atualizem ou expandam a documentação.

---

## 📧 Suporte

Se você encontrar problemas ou tiver dúvidas, abra uma **Issue** no repositório explicando o problema ou entre em contato pelo e-mail:

**[monique.borges1@gmail.com](monique.borges1@gmail.com)**

Obrigado por ajudar a tornar este projeto ainda melhor! 🚀
