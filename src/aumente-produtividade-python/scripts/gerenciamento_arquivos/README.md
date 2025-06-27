# BackupAutomatizado

Este projeto é um script Python que realiza backups automáticos de um arquivo Excel, salvando-os localmente e enviando-os para uma pasta do SharePoint. Além disso, ele inclui funcionalidade de agendamento para execução periódica.

## Índice

1. [Descrição](#descrição)
2. [Requisitos](#requisitos)
3. [Instalação](#instalação)
4. [Uso](#uso)
5. [Funcionamento](#funcionamento)
6. [Boas Práticas](#boas-práticas)
7. [Licença](#licença)

## Descrição

O script:
- Carrega dados de um arquivo Excel.
- Cria backups do arquivo em uma pasta local, com nomes baseados no horário atual.
- Envia os backups para um servidor SharePoint.
- Automatiza o processo de backup em horários específicos (segunda, quarta e sexta às 09:00).

## Requisitos

Certifique-se de ter os seguintes pacotes instalados no seu ambiente Python:

- `pandas`
- `openpyxl`
- `requests`
- `schedule`

Além disso, é necessário:
- Python 3.7 ou superior.
- Permissões de acesso ao SharePoint.

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu_usuario/BackupAutomatizado.git
   cd BackupAutomatizado
   ```

2. Crie um ambiente virtual (opcional, mas recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate   # No Windows: venv\Scripts\activate
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure as URLs e credenciais do SharePoint no script (linha com `sharepoint_url`).

## Uso

Execute o script com:
```bash
python backup_automatizado.py
```

O script será executado continuamente, verificando a necessidade de realizar backups nos horários agendados.

## Funcionamento

### Fluxo principal:
1. **Carregamento de dados**:
   - O arquivo `sales_data.xlsx` é lido usando o `pandas`.

2. **Backup local**:
   - Cria uma cópia do arquivo na pasta `backups/`, com nomes baseados no timestamp.

3. **Upload para o SharePoint**:
   - O backup é enviado para a pasta remota especificada.

4. **Agendamento**:
   - Usando `schedule`, o script roda nos horários especificados (segunda, quarta e sexta às 09:00).

## Boas Práticas

- **Ambiente isolado**:
  Use um ambiente virtual para evitar conflitos de dependências.

- **Manutenção do SharePoint**:
  Verifique periodicamente se a pasta do SharePoint está limpa, removendo arquivos antigos, se necessário.

- **Logs**:
  Adicione logging ao script para monitorar sucessos e falhas, especialmente no upload.

- **Segurança**:
  Não inclua credenciais sensíveis diretamente no código. Use variáveis de ambiente ou um gerenciador de segredos.

- **Testes**:
  Teste o script localmente antes de usá-lo em produção para evitar perda de dados.

- **Backups antigos**:
  Implemente uma rotina para deletar backups locais antigos, se necessário, para economizar espaço.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE). Sinta-se à vontade para usá-lo e modificá-lo conforme necessário.
