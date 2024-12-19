from fastapi import FastAPI
from app.routes import product, user, order
from app.database import engine
from app.models import models

description = """
# E-commerce API

Esta API fornece endpoints para gerenciar um e-commerce básico, incluindo:

## Funcionalidades

### Produtos
* Criar produtos
* Listar produtos
* Buscar produtos específicos
* Atualizar produtos
* Deletar produtos

### Usuários
* Criar conta de usuário
* Autenticar usuários
* Gerenciar perfis
* Visualizar histórico de pedidos

### Pedidos
* Criar pedidos
* Listar pedidos
* Atualizar status de pedidos
* Gerenciar itens do pedido
"""

tags_metadata = [
    {
        "name": "users",
        "description": "Operações com usuários. Inclui registro, autenticação e gerenciamento de perfil.",
    },
    {
        "name": "products",
        "description": "Gerenciar produtos do e-commerce. Inclui criação, listagem, atualização e remoção.",
    },
    {
        "name": "orders",
        "description": "Gerenciar pedidos. Inclui criação de pedidos, atualização de status e listagem.",
    },
]

app = FastAPI(
    title="E-commerce API",
    description=description,
    openapi_tags=tags_metadata
)

models.Base.metadata.create_all(bind=engine)

app.include_router(
    product.router,
    prefix="/api/products",
    tags=["products"]
)

app.include_router(
    user.router,
    prefix="/api/users",
    tags=["users"]
)

app.include_router(
    order.router,
    prefix="/api/orders",
    tags=["orders"]
)

@app.get("/", tags=["root"])
async def read_root():
    """
    Rota raiz que retorna uma mensagem de boas-vindas.
    """
    return {"message": "Bem-vindo à API de E-commerce!"}