from schemas.item import Item
from models.items import Item as ItemDb
import json
from fastapi import APIRouter, Depends
from typing import Optional


router = APIRouter()

from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.get("/")
async def read_items(skip: int = 1, limit: int = 10, token: str = Depends(oauth2_scheme)):
    return {
        "list": json.loads(ItemDb.get_all(skip, limit)),
        "limit": limit,
        "page": skip
    }


@router.get("/{item_id}")
async def read_item(item_id: Optional[str], q: str=None):
    return json.loads(ItemDb.get_item(item_id).to_json())
    # return {"item_id": item_id, "q": q}


@router.put("/{item_id}")
async def update(item_id: str, item: Item):
    item = ItemDb.update_item(item_id, item.dict())
    return json.loads(item.to_json())


@router.post("/")
async def create(item: Item):
    import pdb;pdb.set_trace()
    new_item = ItemDb.save_item(item.dict())
    return json.loads(new_item.to_json())
    # return {"item_name": item.name, "item_id": item.item_id, "price": item.price, "is_offer": item.is_offer}


@router.delete("/{item_id}")
async def delete(item_id: str, item: Item):
    item = ItemDb.delete_item(item_id)
    return {}
