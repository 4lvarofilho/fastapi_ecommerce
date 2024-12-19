# E-commerce API

Uma API RESTful de e-commerce desenvolvida com FastAPI, MySQL e Docker. Este projeto inclui autenticação de usuários, gestão de produtos, pedidos e testes automatizados.

## 🚀 Tecnologias Utilizadas

- **FastAPI**: Framework web moderno e rápido para construção de APIs com Python
- **MySQL**: Sistema de gerenciamento de banco de dados
- **SQLAlchemy**: ORM (Object Relational Mapper) para Python
- **Pytest**: Framework de testes
- **Docker**: Containerização da aplicação
- **Docker Compose**: Orquestração de containers
- **Pydantic**: Validação de dados
- **Uvicorn**: Servidor ASGI para Python

## 📋 Pré-requisitos

- Python 3.8+
- Docker
- Docker Compose
- Git

## 🔧 Estrutura do Projeto

```
ecommerce_api/
│
├── docker/
│   ├── Dockerfile
│   └── docker-compose.yml
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── models.py
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── schemas.py
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── product.py
│   │   ├── user.py
│   │   └── order.py
│   └── database.py
│
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_products.py
│   ├── test_users.py
│   └── test_orders.py
│
├── requirements.txt
├── .env
└── README.md
```

## 🛠️ Instalação e Configuração

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/ecommerce-api.git
cd ecommerce-api
```

2. Crie um arquivo `.env` na raiz do projeto:
```env
DATABASE_URL=mysql+pymysql://user:password@db:3306/ecommerce
SECRET_KEY=your-secret-key-here
```

3. Inicie os containers com Docker Compose:
```bash
docker-compose up --build
```

A API estará disponível em: `http://localhost:8000`

## 📚 Documentação da API

A documentação completa da API está disponível em:

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

### Endpoints Principais

#### Produtos
- `POST /api/products/`: Criar novo produto
- `GET /api/products/`: Listar produtos
- `GET /api/products/{id}`: Obter produto específico
- `PUT /api/products/{id}`: Atualizar produto
- `DELETE /api/products/{id}`: Deletar produto

#### Usuários
- `POST /api/users/`: Criar novo usuário
- `GET /api/users/`: Listar usuários
- `GET /api/users/{id}`: Obter usuário específico
- `DELETE /api/users/{id}`: Deletar usuário

#### Pedidos
- `POST /api/orders/`: Criar novo pedido
- `GET /api/orders/`: Listar pedidos
- `GET /api/orders/{id}`: Obter pedido específico
- `PUT /api/orders/{id}/status`: Atualizar status do pedido

## ⚡ Desenvolvimento

Para desenvolver localmente:

1. Crie um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
.\venv\Scripts\activate  # Windows
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Execute os testes:
```bash
pytest tests/ -v
```

4. Inicie o servidor de desenvolvimento:
```bash
uvicorn app.main:app --reload
```

## 🧪 Testes

O projeto utiliza pytest para testes. Para executar os testes:

```bash
# Executar todos os testes
pytest

# Executar testes com cobertura
pytest --cov=app tests/

# Executar testes específicos
pytest tests/test_products.py -v
```

## 📦 Modelos de Dados

### Product
```python
{
    "id": int,
    "name": str,
    "description": str,
    "price": float,
    "stock": int
}
```

### User
```python
{
    "id": int,
    "email": str,
    "is_active": bool
}
```

### Order
```python
{
    "id": int,
    "user_id": int,
    "items": List[OrderItem],
    "status": str,
    "order_date": datetime
}
```

## 🔐 Segurança

- Senhas são hasheadas antes de serem armazenadas
- Validação de dados com Pydantic
- Proteção contra SQL Injection via SQLAlchemy
- Sanitização de inputs

## 🚀 Deploy

Para deploy em produção:

1. Modifique as configurações em `config.py`
2. Atualize as variáveis de ambiente no `.env`
3. Configure as credenciais do banco de dados
4. Execute com um servidor ASGI como Uvicorn ou Gunicorn

```bash
gunicorn app.main:app -w 4 -k uvicorn.workers.UvicornWorker
```

## 📈 Futuras Melhorias

- [ ] Implementar autenticação JWT
- [ ] Adicionar cache com Redis
- [ ] Implementar sistema de pagamentos
- [ ] Adicionar sistema de avaliações
- [ ] Implementar notificações por email
- [ ] Adicionar logging
- [ ] Implementar sistema de cupons
- [ ] Adicionar relatórios e analytics

## 🤝 Contribuindo

1. Faça um Fork do projeto
2. Crie uma Branch para sua Feature (`git checkout -b feature/AmazingFeature`)
3. Faça o Commit de suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Faça o Push para a Branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request


## ✨ Autor

Álvaro Filho - [@4lvarofilho](https://twitter.com/4lvarofilho)

Project Link: [https://github.com/4lvarofilho/fastapi_ecommerce.git](https://github.com/4lvarofilho/fastapi_ecommerce.git)

## 📧 Contato

- Email: alvarofilho.dev@gmail.com
- LinkedIn: [Álvaro Filho](www.linkedin.com/in/álvaro-filho-3173622b3)