from ariadne import QueryType, MutationType
from .db import SessionLocal, Product

query = QueryType()
mutation = MutationType()

@query.field("products")
def resolve_products(_, info):
    session = SessionLocal()
    products = session.query(Product).all()
    session.close()
    return products

@query.field("product")
def resolve_product(_, info, id):
    session = SessionLocal()
    product = session.query(Product).get(id)
    session.close()
    return product

@mutation.field("createProduct")
def resolve_create_product(_, info, input):
    session = SessionLocal()
    new_product = Product(name=input["name"], price=input["price"])
    session.add(new_product)
    session.commit()
    session.refresh(new_product)
    session.close()
    return new_product

@mutation.field("updateProduct")
def resolve_update_product(_, info, id, input):
    session = SessionLocal()
    product = session.query(Product).get(id)
    if not product:
        session.close()
        return None
    product.name = input["name"]
    product.price = input["price"]
    session.commit()
    session.refresh(product)
    session.close()
    return product

@mutation.field("deleteProduct")
def resolve_delete_product(_, info, id):
    session = SessionLocal()
    product = session.query(Product).get(id)
    if not product:
        session.close()
        return None
    session.delete(product)
    session.commit()
    session.close()
    return product

# Для использования в make_executable_schema:
resolvers = [query, mutation]
