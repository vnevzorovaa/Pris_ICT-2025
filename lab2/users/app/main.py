from fastapi import FastAPI
from ariadne.asgi import GraphQL
from ariadne import make_executable_schema, load_schema_from_path
from app.resolvers import query, mutation
from app.db import database, metadata, users_table
import sqlalchemy
import databases

type_defs = load_schema_from_path("app/schema.graphql")
schema = make_executable_schema(type_defs, query, mutation)

app = FastAPI()
app.mount("/graphql", GraphQL(schema, debug=True))

@app.on_event("startup")
async def startup():
    engine = sqlalchemy.create_engine("postgresql://postgres:postgres@localhost:5432/users")
    metadata.create_all(engine)
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()