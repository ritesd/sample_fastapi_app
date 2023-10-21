from fastapi import FastAPI

from src.prequin_apis import generate_array_api
from src.user_apis import user_auth_api

def import_routes(app: FastAPI) -> None:
    # user auth apis
    app.include_router(user_auth_api.router)

    # prequin_apis
    app.include_router(generate_array_api.router)