from fastapi import FastAPI

from app.database.connection import engine
from app.database.base import Base

from app.routes.usuario_route import router as usuario_router
from app.routes.pedido_route import router as pedido_router

from app.models.usuario import Usuario
from app.models.pedido import Pedido


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="DimDim API"
)

app.include_router(usuario_router)

app.include_router(pedido_router)


@app.get("/")
def home():

    return {
        "mensagem": "DimDim API funcionando"
    }