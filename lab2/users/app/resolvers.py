from ariadne import QueryType, MutationType
from app.db import database, users_table
import sqlalchemy

query = QueryType()
mutation = MutationType()

@query.field("users")
async def resolve_users(_, info):
    query = users_table.select()
    return await database.fetch_all(query)

@query.field("user")
async def resolve_user(_, info, id):
    query = users_table.select().where(users_table.c.id == int(id))
    return await database.fetch_one(query)

@mutation.field("createUser")
async def resolve_create_user(_, info, name, email):
    query = users_table.insert().values(name=name, email=email)
    user_id = await database.execute(query)
    return { "id": user_id, "name": name, "email": email }

@mutation.field("updateUser")
async def resolve_update_user(_, info, id, name=None, email=None):
    values = {}
    if name: values["name"] = name
    if email: values["email"] = email
    query = users_table.update().where(users_table.c.id == int(id)).values(**values)
    await database.execute(query)
    return await resolve_user(_, info, id)

@mutation.field("deleteUser")
async def resolve_delete_user(_, info, id):
    query = users_table.delete().where(users_table.c.id == int(id))
    await database.execute(query)
    return True
    return True
