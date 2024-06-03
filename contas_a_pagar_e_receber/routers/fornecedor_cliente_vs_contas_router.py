from sqlalchemy.orm import Session
from typing import List
from fastapi import APIRouter, Depends
from contas_a_pagar_e_receber.models.conta_a_pagar_receber_model import ContaPagarReceber
from contas_a_pagar_e_receber.routers.contas_a_pagar_e_receber_router import ContaPagarReceberResponse
from shared.dependencies import get_db

router = APIRouter(prefix="/fornecedor-cliente")

@router.get("/{id_fornecedor_cliente}/contas-a-pagar-e-receber", response_model=List[ContaPagarReceberResponse], status_code=200)
async def obter_contas_a_pagar_fornecedor_cliente_id(id_fornecedor: int, db:Session=Depends(get_db)) -> List[ContaPagarReceberResponse]:
    response_db = db.query(ContaPagarReceber).filter_by(fornecedor_cliente_id=id_fornecedor).all()
    return response_db