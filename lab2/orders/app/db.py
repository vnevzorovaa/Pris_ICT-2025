from motor.motor_asyncio import AsyncIOMotorClient

MONGO_DETAILS = "mongodb://mongo:27017"
client = AsyncIOMotorClient(MONGO_DETAILS)
database = client.orders_db
orders_collection = database.get_collection("orders")
async def fetch_one_order(id):
    document = await orders_collection.find_one({"id": id})
    return document