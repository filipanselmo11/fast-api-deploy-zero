from fastapi import FastAPI

from contas_a_pagar_e_receber.routers import contas_a_pagar_e_receber_router

app = FastAPI()

app.include_router(contas_a_pagar_e_receber_router.router)