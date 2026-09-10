from pymongo import MongoClient
from datetime import datetime

from src.schemas import OrderRequest, OrderResult, OrderStatus


class PostIts:
    def __init__(self) -> None:
        # TODO:
        # document_class: default class to use for
        # documents returned from queries on this client
        self.client = MongoClient(
            host="127.0.0.1", port=27017, username="restaurant", password="restaurant"
        )
        self.collection = self.client.order_db.tasks

    def append(self, order: OrderRequest):
        self.collection.insert_one(
            {
                "_id": order.id,
                **order.model_dump(),
                "created_at": datetime.utcnow(),
                "updated_at": datetime.utcnow(),
            }
        )

    def update(self, order_id: str, status: OrderStatus):
        self.collection.update_one(
            {"_id": order_id},
            {"$set": {"status": status, "updated_at": datetime.utcnow()}},
        )

    def get(self, order_id: str) -> OrderRequest | None:
        doc = self.collection.find_one({"_id": order_id})
        if doc is None:
            return None
        ret = OrderRequest(**doc)
        return ret


post_its = PostIts()
