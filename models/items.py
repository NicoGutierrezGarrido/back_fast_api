from mongoengine import *
from fastapi import FastAPI, HTTPException

# connect('mongodb://host.docker.internal:27017/checklists')
connect(
    'checklists',
    host='host.docker.internal'
)


class Item(Document):
    name = StringField(required=True)
    price = DecimalField(max_length=50)
    is_offer = BooleanField()

    @classmethod
    def get_item(cls, _id: str, as_json: bool = False):
        item = Item.objects(id=_id).first()
        if not item:
            raise HTTPException(status_code=404, detail="Item not found")
        return item

    @classmethod
    def get_all(cls, skip, limit):
        page_nb = skip
        items_per_page = limit
        offset = (page_nb - 1) * items_per_page
        q_set = Item.objects.skip(offset).limit(items_per_page)
        json_data = q_set.to_json()
        return json_data

    @classmethod
    def save_item(cls, data: dict):
        item = Item(**data).save()
        return item

    @classmethod
    def update_item(cls, _id: str, data: dict):
        item = Item.get_item(_id)
        for k, v in data.items():
            setattr(item, k, v)
        item.save()
        return item

    @classmethod
    def delete_item(cls, _id: str):
        item = Item.get_item(_id)
        item.delete()


class Users(Document):
    name = StringField()
    email = EmailField()
    password = StringField()