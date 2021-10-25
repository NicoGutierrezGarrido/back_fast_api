from fastapi import APIRouter
from typing import Optional
from models.item import Item
import json

router = APIRouter()


@router.get("/")
async def read_items(skip: int = 1, limit: int = 10):
    return {
        "list": json.loads(Item.get_all(skip, limit)),
        "limit": limit,
        "page": skip
    }


@router.get("/{item_id}")
async def read_item(item_id: Optional[str], q: str=None):
    return json.loads(Item.get_item(item_id).to_json())