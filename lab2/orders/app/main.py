from fastapi import FastAPI
from ariadne.asgi import GraphQL
from ariadne import make_executable_schema, QueryType

query = QueryType()

@query.field("hello")
def resolve_hello(_, info):
    return "Hello, GraphQL!"

type_defs = """
    type Query {
        hello: String!
    }
"""

schema = make_executable_schema(type_defs, query)

app = FastAPI()
app.mount("/graphql", GraphQL(schema, debug=True))
#app.mount("/docs", SwaggerUIHTMLFactory(app))