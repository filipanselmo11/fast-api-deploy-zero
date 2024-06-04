from typing import List
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from contas_a_pagar_e_receber.models.fornecedor_cliente_model import FornecedorCliente
from shared.dependencies import get_db
from shared.exceptions import NotFound


router = APIRouter(prefix="/fornecedor-cliente")

class FornecedorClienteResponse(BaseModel):
    id: int
    nome: str

    class Config:
        from_attributes = True

class FornecedorClienteRequest(BaseModel):
    nome: str

@router.get("/", response_model=List[FornecedorClienteResponse], status_code=200)
async def listar_fornecedores(db: Session = Depends(get_db)) -> List[FornecedorClienteResponse]:
    return db.query(FornecedorCliente).all()

@router.get("/{id_fornecedor_cliente}", response_model=FornecedorClienteResponse, status_code=200)
async def obter_um_fornecedor(id_fornecedor: int, db:Session=Depends(get_db)) -> FornecedorClienteResponse:
    fornecedor_cliente = busca_fornecedor_por_id(id_fornecedor, db)
    return fornecedor_cliente


@router.post("", response_model=FornecedorClienteResponse, status_code=201)
async def criar_fornecedor(fornecedor_cliente_request:FornecedorClienteRequest, db: Session = Depends(get_db)) -> FornecedorClienteResponse:
    fornecedor_cliente = FornecedorCliente(**fornecedor_cliente_request.model_dump())
    db.add(fornecedor_cliente)
    db.commit()
    db.refresh(fornecedor_cliente)
    return fornecedor_cliente

@router.put("/{id_fornecedor_cliente}", response_model=FornecedorClienteResponse, status_code=200)
async def atualizar_fornecedor(id_fornecedor_cliente: int, fornecedor_cliente_request:FornecedorClienteRequest, db: Session = Depends(get_db)) -> FornecedorClienteResponse:
    fornecedor_cliente = busca_fornecedor_por_id(id_fornecedor_cliente, db)
    fornecedor_cliente.nome = fornecedor_cliente_request.nome
    db.add(fornecedor_cliente.nome)
    db.commit()
    db.refresh(fornecedor_cliente.nome)
    return fornecedor_cliente.nome

@router.delete("/{id_fornecedor_cliente}", status_code=204)
async def deletar_conta(id_fornecedor_cliente: int, db: Session = Depends(get_db)) -> None:
    fornecedor_cliente = busca_fornecedor_por_id(id_fornecedor_cliente, db)
    db.delete(fornecedor_cliente)
    db.commit()
    #return fornecedor_cliente



def busca_fornecedor_por_id(id: int, db: Session) -> FornecedorCliente:
    fornecedor_cliente = db.query(FornecedorCliente).get(id)
    if fornecedor_cliente is None:
        raise NotFound("Fornecedor")
    return fornecedor_cliente