from sqlalchemy import Column, ForeignKey, Integer, Numeric, String
from shared.database import Base
from sqlalchemy.orm import relationship


class ContaPagarReceber(Base):
    __tablename__ = "contas_a_pagar_e_receber"
    id = Column(Integer, primary_key=True, autoincrement=True)
    desc = Column(String(30))
    valor = Column(Numeric)
    tipo = Column(String(30))
    fornecedor_cliente_id = Column(Integer, ForeignKey("fornecedor_cliente.id"))
    fornecedor = relationship("FornecedorCliente")