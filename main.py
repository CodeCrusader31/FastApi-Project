from fastapi import FastAPI
from models import Product
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}


products = [
    {"id": 1, "name": "Product 1","description":"iphone", "price": 99.0,"quantity":10},
    {"id": 2, "name": "Product 2", "description" :"asus laptop", "price": 999.0, "quantity":20},
    {"id": 3, "name": "Product 3","description":"poco m3", "quantity":12, "price": 30.0},
    {"id": 4, "name": "Product 4", "description":"samsung s20", "quantity":15, "price": 500.0}
]

@app.get("/products")
def get_products():
    return products

@app.get("/products/{id}")
def get_product_by_id(id: int):
    for product in products:
        if product["id"] == id:
            return product
    return "Product not found"


@app.post("/product")
def add_product(product: Product):
    products.append(product)
    return product
    #return {"message": "Product added successfully"}


@app.put("/product/{id}")
def update_product(id: int, product: Product):
    for i in range(len(products)):
        if products[i]["id"] == id:
            products[i] = product.model_dump()
            return {"message": "Product Updated Successfully"}

    return {"message": "Product Not Found"}


@app.delete("/product")
def delete_product(id: int):
    for i in range(len(products)):
        if(products[i]["id"]) == id:
            del products[i]
            return "Product deleted"
    return "Product not found"