from fastapi import APIRouter, HTTPException

from app.controllers.controllers import search_municipio

router = APIRouter()


@router.get("/autocomplete")
async def autocomplete(q: str | None = None):
    if q is None:
        raise HTTPException("QueryCantBeNone")
    elif len(q) < 3:
        raise HTTPException("QueryMustBeGreaterThan3Characters")
    
    return await search_municipio(query=q)