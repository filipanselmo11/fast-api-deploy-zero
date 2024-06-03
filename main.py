from fastapi import FastAPI
from contas_a_pagar_e_receber.routers import contas_a_pagar_e_receber_router, fornecedor_cliente_router, fornecedor_cliente_vs_contas_router
from shared.exceptions import NotFound
from shared.exceptions_handler import not_found_handler

# from shared.database import Base, engine
# from contas_a_pagar_e_receber.models.conta_a_pagar_receber_model import ContaPagarReceber

# Base.metadata.drop_all(bind=engine)
# Base.metadata.create_all(bind=engine)


app = FastAPI()

app.include_router(contas_a_pagar_e_receber_router.router)
app.include_router(fornecedor_cliente_router.router)
app.include_router(fornecedor_cliente_vs_contas_router.router)
app.add_exception_handler(NotFound, not_found_handler)



