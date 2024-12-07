# Vermax API

#### A simple and secure "Home broker API" for managing user accounts, deposits, balances, and asset purchases.

___

## Iniciando o projeto

Abaixo estão os métodos para execução do serviço via Poetry ou Docker. O método recomendado é o Docker.

- **Python**: Python 3.12
- **Docker**: Docker version 27.2.0
- **Docker Compose**: v2.29.2-desktop.2

### Observação:
- O arquivo `.env` foi incluído no repositório para facilitar os testes. **Não é uma boa prática**.

___

## Iniciando o projeto com Docker

Certifique-se de estar no diretório raiz do projeto.

Execute o comando abaixo para subir os serviços da API e do PostgreSQL:

```bash
docker-compose up -d
```

Verifique se os serviços estão funcionando:  
```bash  
docker-compose ps  
```  

Você verá uma saída semelhante a:  
```bash  
NAME                  IMAGE          COMMAND                  SERVICE   CREATED         STATUS         PORTS
vermax-postgres-db    postgres       "docker-entrypoint.s…"   db        1 minute ago    Up 2 seconds   0.0.0.0:5432->5432/tcp
vermax-api           vermax-api     "poetry run python3 …"    api       1 minute ago    Up 2 seconds   0.0.0.0:8000->8000/tcp
```  
___  

## Iniciando o projeto com Poetry
(caso prefira subir apenas o container do db e rodar aplicação no seu terminal/editor)

### Passo 1  
Instale o Poetry (https://python-poetry.org/docs/).  

### Passo 2  
Entre no diretório raiz do projeto e crie o ambiente virtual:  
```bash  
poetry shell  
```  

### Passo 3  
Instale as dependências:  
```bash  
poetry install  
```  

### Passo 4  
Suba o serviço do PostgreSQL necessário para persistência:  
```bash  
docker-compose up -d db  
```

### Passo 5  
Rode o alembic, para aplicar migration e criar tabelas:  
```bash  
alembic upgrade head
```

### Passo 6  
Inicie a aplicação:  
```bash  
python3 main.py  
```  

Você verá uma saída semelhante em ambos os cenários:  
```bash  
vermax-api          | INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
vermax-api          | INFO  [alembic.runtime.migration] Will assume transactional DDL.
vermax-api          | INFO  [alembic.runtime.migration] Running upgrade  -> 5d7b7043be93, create tables
vermax-api          | Tables found: dict_keys(['accounts', 'users', 'transactions'])
vermax-api          | Skipping virtualenv creation, as specified in config file.
vermax-api          | Server is ready at URL 0.0.0.0:8000/home-broker/v1
vermax-api          |                                                       _
vermax-api          | __   _____ _ __ _ __ ___   __ ___  __      __ _ _ __ (_)
vermax-api          | \ \ / / _ \ '__| '_ ` _ \ / _` \ \/ /____ / _` | '_ \| |
vermax-api          |  \ V /  __/ |  | | | | | | (_| |>  <_____| (_| | |_) | |
vermax-api          |   \_/ \___|_|  |_| |_| |_|\__,_/_/\_\     \__,_| .__/|_|
vermax-api          |                                                |_|
vermax-api          |
vermax-api          | INFO:     Started server process [10]
vermax-api          | INFO:     Waiting for application startup.
vermax-api          | INFO:     Application startup complete.
vermax-api          | INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
```  
___  

## Swagger - Documentação  

Acesse a documentação interativa gerada no link:
> [http://localhost:8000/home-broker/v1/docs](http://localhost:8000/home-broker/v1/docs)) 
___  

## Padrão de Resposta  

Todas as respostas da API seguem um padrão consistente, garantindo uma fácil interpretação dos resultados e dos possíveis erros.  

### Estrutura de Resposta  

```json  
{
  "success": true,
  "message": "Operação realizada com sucesso",
  "payload": {
    // Dados específicos da resposta
  }
}
```  

### Descrição dos Campos  

- **success**: Indica o resultado geral da operação.  
  - `true`: A operação foi concluída com sucesso.  
  - `false`: Ocorreu um erro na operação.  

- **message**: Mensagem explicativa sobre o resultado da operação ou para servir o client/front.  
  - Exemplo: `"Operação realizada com sucesso"` ou `"Erro ao processar a solicitação"`.  

- **payload**: Dados retornados pela operação.  
 - Pode conter objetos específicos, listas ou informações adicionais dependendo da requisição realizada.  


### Exemplo de Resposta de Sucesso  
```json  
{
  "success": true,
  "payload": {
    "account_id": "92240ccc-a778-4f9d-b2af-cb9f3caf6e80",
    "name": "Vinicius dos Reisx",
    "email": "vih-reis@hotmail.com",
    "cpf": "41588156818",
    "id": 1
  }
} 
```  

### Exemplo de Resposta de Erro  
```json  
{
  "success": false,
  "message": "User with ID 5 not found."
}
```

## Endpoints  

### Users  

#### 1. Listar usuários paginados
- **Rota**: `GET /home-broker/v1/users`
- **Descrição**: Lista usuários com paginação.

**Parâmetros de consulta**:
| Parâmetro | Descrição       | Obrigatório | Exemplo |
|-----------|-----------------|-------------|---------|
| limit     | Limite de itens | Não         | 10      |
| offset    | Offset inicial  | Não         | 0       |

**Resposta**:
```json
{
  "success": true,
  "message": "Users retrieved successfully",
  "status_code": 200,
  "payload": {
    "users": [
      {
        "account_id": "123e4567-e89b-12d3-a456-426614174000",
        "name": "John Doe",
        "email": "john@example.com",
        "cpf": "12345678900",
        "id": 1
      }
    ],
    "total": 1,
    "limit": 10,
    "offset": 0
  }
} 
```  

#### 2. Criar novo usuário  
- **Rota**: `POST /home-broker/v1/users`  
- **Descrição**: Cria um novo usuário.  

**Parâmetros do corpo da requisição**:  
| Parâmetro | Descrição       | Obrigatório | Exemplo           |  
|-----------|-----------------|-------------|------------------ |  
| name      | Nome do usuário | Sim         | "John Doe"        |  
| email     | Email do usuário| Sim         | "john@example.com"|  
| cpf       | CPF do usuário  | Sim         | "123.456.789-00"  |
| password  | Senha do usuário| Sim         | "102030"          |  

**Resposta**:  
```json  
{
  "success": true,
  "message": "User created successfully",
  "status_code": 201,
  "payload": {
    "account_id": "123e4567-e89b-12d3-a456-426614174000",
    "id": 1
  }
}  
```  

#### 3. Obter um usuário específico  
- **Rota**: `GET /home-broker/v1/users/{user_id}`  
- **Descrição**: Retorna detalhes de um usuário específico.
- **Autenticação**: Bearer Token necessário.

**Parâmetro de caminho**:  
| Parâmetro | Descrição       | Obrigatório | Exemplo |  
|-----------|-----------------|-------------|---------|  
| user_id   | ID do usuário   | Sim         | 1       |  

**Resposta**:  
```json  
{
  "success": true,
  "message": "User retrieved successfully",
  "status_code": 200,
  "payload": {
    "account_id": "123e4567-e89b-12d3-a456-426614174000",
    "name": "John Doe",
    "email": "john@example.com",
    "cpf": "12345678900",
    "id": 1
  }
}  
```  

#### 4. Atualizar um usuário  
- **Rota**: `PUT /home-broker/v1/users/{user_id}`  
- **Descrição**: Atualiza as informações de um usuário existente.
- **Autenticação**: Bearer Token necessário.

**Parâmetro de caminho**:  
| Parâmetro | Descrição       | Obrigatório | Exemplo |  
|-----------|-----------------|-------------|---------|  
| user_id   | ID do usuário   | Sim         | 1       |  

**Parâmetros do corpo da requisição**:  
| Parâmetro | Descrição       | Obrigatório | Exemplo          |  
|-----------|-----------------|-------------|------------------|  
| name      | Nome do usuário | Sim         | "John Updated"   |  
| email     | Email do usuário| Sim         | "john2@example.com"|  

**Resposta**:  
```json  
{  
  "success": true,  
  "message": "User updated successfully",  
}  
```  

#### 5. Deletar um usuário  
- **Rota**: `DELETE /home-broker/v1/users/{user_id}`  
- **Descrição**: Deleta um usuário existente.
- **Autenticação**: Bearer Token necessário.

**Parâmetro de caminho**:  
| Parâmetro | Descrição       | Obrigatório | Exemplo |  
|-----------|-----------------|-------------|---------|  
| user_id   | ID do usuário   | Sim         | 1       |  

**Resposta**:  
```json  
{
  "success": true,
  "message": "User deleted successfully",
}  
```
## Accounts

#### 1. Realizar transferência
- **Rota**: `POST /home-broker/v1/accounts/transfer`
- **Descrição**: Realiza transferência entre contas.
- **Autenticação**: Bearer Token necessário

**Parâmetros do corpo da requisição**:
| Parâmetro         | Descrição             | Obrigatório| Exemplo    |
|-------------------|-----------------------|------------|------------|
| operation         | Tipo de operação      | Sim        | "TRANSFER" |
| amount            | Valor da transferência| Sim        | 100.00     |
| target.bank       | Banco destino         | Sim        | "001"      |
| target.branch     | Agência destino       | Sim        | "0001"     |
| target.account_id | UUID da conta destino | Sim        | "123e4567-e89b-12d3-a456-426614174000" |
| origin.bank       | Banco origem          | Sim        | "001"      |
| origin.branch     | Agência origem        | Sim        | "0001"     |

**Resposta**:
```json
{
  "success": true,
  "message": "Transfer completed successfully",
  "status_code": 200,
  "payload": {
    "transaction_id": "123e4567-e89b-12d3-a456-426614174000",
    "account_id": "123e4567-e89b-12d3-a456-426614174000",
    "amount": "100.00",
    "operation": "TRANSFER",
    "created_at": "2024-01-01T10:00:00"
  }
}
```
#### 2. Consultar saldo e posições (não implementado posicoes e saldo consolidado)
- **Rota**: `GET /home-broker/v1/accounts/balance`
- **Descrição**: Retorna o saldo atual da conta, posições em ativos e saldo consolidado.
- **Autenticação**: Bearer Token necessário

**Resposta**:
```json
{
  "success": true,
  "message": "Balance retrieved successfully",
  "status_code": 200,
  "payload": {
    "balance": "1000.00",
    "positions": {
      "PETR4": {
        "quantity": 100,
        "average_price": "28.50"
      }
    },
    "consolidated_balance": "3850.00"
  }
}
```
### Authentication

#### 1. Obter Token de Acesso
- **Rota**: `POST /home-broker/v1/token`
- **Descrição**: Gera um token de acesso para autenticação nas rotas protegidas.

**Parâmetros do formulário**:
| Parâmetro | Descrição         | Obrigatório | Exemplo            |
|-----------|-------------------|-------------|--------------------|
| username  | Email do usuário  | Sim         | "user@example.com" |
| password  | Senha do usuário  | Sim         | "senha123"         |

**Resposta**:
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```
___  

## HttpStatusCode  

### OK  
- **Código HTTP:** `200 Success`  
- Para requisições bem-sucedidas.  

### Created  
- **Código HTTP:** `201 Created`  
- Para criação de recursos com sucesso.  

### BadRequest  
- **Código HTTP:** `400 Bad Request`  
- Problema na sintaxe ou semântica da requisição.

### UnprocessableContent
- **Código HTTP:** `422 Unprocessable Content`  
- Sintaxe/semântica ok mas fere alguma regra de negócio.  

### InternalServerError  
- **Código HTTP:** `500 Internal Server Error`  
- Erro inesperado no servidor.  
___  
