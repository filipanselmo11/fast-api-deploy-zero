from decimal import Decimal
from typing import List
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from contas_a_pagar_e_receber.models.conta_a_pagar_receber_model import ContaPagarReceber
from shared.dependencies import get_db
from shared.exceptions import NotFound


router = APIRouter(prefix="/contas-a-pagar-e-receber")

class ContaPagarReceberResponse(BaseModel):
    id: int
    desc: str
    valor: Decimal
    tipo: str

    class Config:
        from_attributes = True

class ContaPagarReceberRequest(BaseModel):
    desc: str
    valor: Decimal
    tipo: str
    fornecedor_cliente_id: int | None = None

@router.get("/", response_model=List[ContaPagarReceberResponse], status_code=200)
async def listar_contas(db: Session = Depends(get_db)) -> List[ContaPagarReceberResponse]:
    return db.query(ContaPagarReceber).all()

@router.get("/{id_contar_pagar_receber}", response_model=ContaPagarReceberResponse, status_code=200)
async def obter_uma_conta(id_conta_pagar_receber: int, db:Session=Depends(get_db)) -> ContaPagarReceberResponse:
    conta_pagar_receber = busca_conta_por_id(id_conta_pagar_receber, db)
    return conta_pagar_receber

@router.post("", response_model=ContaPagarReceberResponse, status_code=201)
async def criar_conta(conta_a_pagar_e_receber_request:ContaPagarReceberRequest, db: Session = Depends(get_db)) -> ContaPagarReceberResponse:
    conta_pagar_receber = ContaPagarReceber(**conta_a_pagar_e_receber_request.model_dump())
    db.add(conta_pagar_receber)
    db.commit()
    db.refresh(conta_pagar_receber)
    return conta_pagar_receber

@router.put("/{id_contar_pagar_receber}", response_model=ContaPagarReceberResponse, status_code=200)
async def atualizar_conta(id_conta_pagar_receber: int, conta_a_pagar_e_receber_request:ContaPagarReceberRequest, db: Session = Depends(get_db)) -> ContaPagarReceberResponse:
    conta_pagar_receber = busca_conta_por_id(id_conta_pagar_receber, db)
    conta_pagar_receber.tipo = conta_a_pagar_e_receber_request.tipo
    conta_pagar_receber.valor = conta_a_pagar_e_receber_request.valor
    conta_pagar_receber.desc = conta_a_pagar_e_receber_request.desc
    db.add(conta_pagar_receber)
    db.commit()
    db.refresh(conta_pagar_receber)
    return conta_pagar_receber

@router.delete("/{id_contar_pagar_receber}", status_code=204)
async def deletar_conta(id_conta_pagar_receber: int, db: Session = Depends(get_db)) -> None:
    conta_pagar_receber = busca_conta_por_id(id_conta_pagar_receber, db)
    db.delete(conta_pagar_receber)
    db.commit()
    #return conta_pagar_receber



def busca_conta_por_id(id: int, db: Session) -> ContaPagarReceber:
    conta_pagar_receber = db.query(ContaPagarReceber).get(id)
    if conta_pagar_receber is None:
        raise NotFound("Conta a pagar e receber")
    return conta_pagar_receber