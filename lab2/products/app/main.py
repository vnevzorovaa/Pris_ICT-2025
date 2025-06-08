from fastapi import FastAPI
from ariadne.asgi import GraphQL
from ariadne import load_schema_from_path, make_executable_schema
from .resolvers import resolvers
from .db import init_db

type_defs = load_schema_from_path("app/schema.graphql")
schema = make_executable_schema(type_defs, *resolvers)

init_db()

app = FastAPI()
app.mount("/graphql", GraphQL(schema, debug=True))
app.mount("/admin", AdminPanel())