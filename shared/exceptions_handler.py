from fastapi import Request
from fastapi.responses import JSONResponse
from shared.exceptions import NotFound

async def not_found_handler(request: Request, exc: NotFound):
    return JSONResponse(
        status_code=404,
        content={"message":f"Ops! {exc.name} não econtrado(a)"}
    )