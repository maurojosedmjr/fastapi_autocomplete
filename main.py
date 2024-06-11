from fastapi import FastAPI

from app.routes.autocomplete import router as autocomplete_route

app = FastAPI()

app.include_router(autocomplete_route)
