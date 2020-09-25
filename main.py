from fastapi import FastAPI, HTTPException

from routers import items

app = FastAPI()
app.include_router(
    items.router,
    prefix="/items",
    tags=["items"]
)
# app.include_router(
#     items.router,
#     prefix="/items",
#     tags=["items"],
#     dependencies=[Depends(get_token_header)],
#     responses={404: {"description": "Not found"}},
# )
