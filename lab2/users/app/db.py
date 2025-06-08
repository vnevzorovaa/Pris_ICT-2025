import sqlalchemy
from databases import Database

DATABASE_URL = "postgresql+asyncpg://postgres:postgres@localhost:6432/users"

database = Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

users_table = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String),
    sqlalchemy.Column("email", sqlalchemy.String),
)

async def get_user(user_id: int) -> dict:
    query = users_table.select().where(users_table.c.id == user_id)
    return await database.fetch_one(query)

async def create_user(name: str, email: str) -> dict:
    query = users_table.insert().values(name=name, email=email)
    return await database.execute(query)

async def update_user(user_id: int, name: str, email: str) -> dict:
    query = users_table.update().where(users_table.c.id == user_id).values(name=name, email=email)
    return await database.execute(query)

async def delete_user(user_id: int) -> dict:
    query = users_table.delete().where(users_table.c.id == user_id)
    return await database.execute(query)