from sqlalchemy import Column, Integer, String, ForeignKey, Numeric
from sqlalchemy.orm import relationship

from app.database.base import Base


class Pedido(Base):

    __tablename__ = "pedidos"

    id = Column(Integer, primary_key=True, index=True)

    descricao = Column(String, nullable=False)

    valor = Column(Numeric(10, 2), nullable=False)

    usuario_id = Column(Integer, ForeignKey("usuarios.id"))

    usuario = relationship("Usuario", back_populates="pedidos")