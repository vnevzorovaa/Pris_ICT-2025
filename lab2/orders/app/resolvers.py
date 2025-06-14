from ariadne import QueryType, MutationType
from app.db import orders_collection
from bson import ObjectId

query = QueryType()
mutation = MutationType()

def order_helper(order) -> dict:
    return {
        "id": str(order["_id"]),
        "userId": order["userId"],
        "product": order["product"],
        "quantity": order["quantity"],
    }

@query.field("orders")
async def resolve_orders(_, info):
    try:
        orders = []
        async for order in orders_collection.find():
            orders.append(order_helper(order))
        return orders
    except Exception as e:
        print("Error in resolve_orders:", e)
        return []

@query.field("order")
async def resolve_order(_, info, id):
    order = await orders_collection.find_one({"_id": ObjectId(id)})
    if order:
        return order_helper(order)
    return None

@mutation.field("createOrder")
async def resolve_create_order(_, info, userId, product, quantity):
    try:
        new_order = {
            "userId": userId,
            "product": product,
            "quantity": quantity,
        }
        result = await orders_collection.insert_one(new_order)
        print("Inserted:", result.inserted_id)

        if not result.inserted_id:
            print("Insertion failed")

        response = {"id": str(result.inserted_id), **new_order}
        print("CreateOrder response:", response)
        return response
    except Exception as e:
        print("Exception in createOrder:", e)
        return None




@mutation.field("deleteOrder")
async def resolve_delete_order(_, info, id):
    result = await orders_collection.delete_one({"_id": ObjectId(id)})
    return result.deleted_count == 1

__all__ = ["query", "mutation"]