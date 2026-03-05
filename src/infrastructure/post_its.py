from pymongo import MongoClient
from datetime import datetime

from src.schemas import OrderRequest, OrderResult


class PostIts:
    def __init__(self) -> None:
        # TODO:
        # document_class: default class to use for
            # documents returned from queries on this client
        self.client = MongoClient(host="127.0.0.1", port=27017, username="restaurant", password="restaurant")
        self.collection = self.client.order_db.tasks

    def append(self, order: OrderRequest):
        self.collection.insert_one(
            {
                "_id": order.id,
                **order.model_dump(),
                "result": None,
                "created_at": datetime.utcnow(),
                "updated_at": datetime.utcnow()
            }
        )

    def update(self, order_id: str, result: OrderResult):
        self.collection.update_one(
            {"_id": order_id},
            {"$set": {"status": result.status, "updated_at": datetime.utcnow()}}
        )

    def get(self, order_id: str):
        return self.collection.find_one({"_id": order_id})
    
post_its = PostIts()