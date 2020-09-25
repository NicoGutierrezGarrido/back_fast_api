from fastapi import APIRouter
from typing import Optional
from model.users import Users

router = APIRouter()


@router.get("/")
async def read_items(skip: int = 1, limit: int = 10):
    return {
        "list": json.loads(ItemDb.get_all(skip, limit)),
        "limit": limit,
        "page": skip
    }


@router.get("/{item_id}")
async def read_item(item_id: Optional[str], q: str=None):
    return json.loads(ItemDb.get_item(item_id).to_json())