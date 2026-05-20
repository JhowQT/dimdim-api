from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import SessionLocal
from app.models.pedido import Pedido
from app.schemas.pedido_schema import (
    PedidoCreate,
    PedidoResponse
)

router = APIRouter()


def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


@router.post("/pedidos", response_model=PedidoResponse)
def criar_pedido(
    pedido: PedidoCreate,
    db: Session = Depends(get_db)
):

    novo_pedido = Pedido(
        descricao=pedido.descricao,
        valor=pedido.valor,
        usuario_id=pedido.usuario_id
    )

    db.add(novo_pedido)

    db.commit()

    db.refresh(novo_pedido)

    return novo_pedido


@router.get("/pedidos", response_model=list[PedidoResponse])
def listar_pedidos(db: Session = Depends(get_db)):

    pedidos = db.query(Pedido).all()

    return pedidos