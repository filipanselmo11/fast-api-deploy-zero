from decimal import Decimal
from typing import List
from fastapi import APIRouter
from pydantic import BaseModel


router = APIRouter(prefix="/contas-a-pagar-e-receber")

class ContaPagarReceberResponse(BaseModel):
    id: int
    desc: str
    valor: Decimal
    tipo: str

class ContaPagarReceberRequest(BaseModel):
    desc: str
    valor: Decimal
    tipo: str

@router.get("/", response_model=List[ContaPagarReceberResponse])
async def listar_contas():
    return [
        ContaPagarReceberResponse(id=1, desc="Conta de luz", valor=1000.50, tipo="pagar"),
        ContaPagarReceberResponse(id=2, desc="Aluguel", valor=1000.50, tipo="pagar"),
    ]

@router.post("", response_model=ContaPagarReceberResponse, status_code=201)
async def criar_conta(conta:ContaPagarReceberRequest):
    return ContaPagarReceberResponse(id=1, desc=conta.desc, valor=conta.valor, tipo=conta.tipo)
