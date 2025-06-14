from fastapi import FastAPI
from ariadne.asgi import GraphQL
from ariadne import QueryType, MutationType, make_executable_schema, load_schema_from_path
from app.resolvers import query, mutation

query = QueryType()
mutation = MutationType()

type_defs = load_schema_from_path("app/schema.graphql")

schema = make_executable_schema(type_defs, query, mutation)

app = FastAPI()
app.mount("/graphql", GraphQL(schema, debug=True))
#app.mount("/docs", SwaggerUIHTMLFactory(app))