from fastapi import FastAPI
from app.routes import product, user, order
from app.database import engine
from app.models import models

app = FastAPI(title="E-commerce API")

models.Base.metadata.create_all(bind=engine)

app.include_router(product.router, prefix="/api/products", tags=["products"])
app.include_router(user.router, prefix="/api/users", tags=["users"])
app.include_router(order.router, prefix="/api/orders", tags=["orders"])