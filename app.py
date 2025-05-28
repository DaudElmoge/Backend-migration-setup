# IMPORT FASTAPI PACKAGE
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import session
from models import get_db, Product, Category
from schemas import ProductSchema,CategorySchema

# initialize it
app = FastAPI()

# allow network request from all servers
app.add_middleware(CORSMiddleware, allow_origins=["http://localhost:5173/"], allow_methods=["http://localhost:5173/"])


# DEFINE ROUTES
# http://localhost:8000/products ->GET
@app.get("/")
def index():
    return {"message": "Welcome to my first backend app"}


# products
# http://localhost:8000/products -> GET -> get all products
@app.get("/products")
def products(session=Depends(get_db)):
    # retrieves all products from the table
    products = session.query(Product).all()
    # categories=session.quert(Category).all()
    # use sqlalchemy to retrireve all products from the db
    return products


# http://localhost:8000/products ->POST
app.post("/products")


def add_products(product: ProductSchema, session: session=Depends(get_db)):
    # 1.create an instance of the product model with the values sent
    #new_product = Product(
        #name=product.name,
        #price=product.price,
        #image=product.image,
        #catergory_id=product.category_id,
    #)
    new_product = Product(**product.model_dump())

    #2. add the product the transaction
    session.add(new_product)
    #3. commit the transaction
    session.commit()
    return {"message": "product created sucessfully"}


# http://localhost:8000/products/3 -> GET -> gets a single product
@app.get("/products/{id}")
def get_product(id: int):
    print("Product id", id)
    return {}


# http://localhost:8000/products/3 -> PATCH/PUT -> update a single product
@app.patch("/products/{id}")
def update_product(id: int):
    print(f"Product of id {id} updated")
    return {"message": "Product updated successfully"}


# http://localhost:8000/products/3 -> DELETE -> delete a single product
@app.delete("/products/{id}")
def delete_product(id: int):
    print(f"Product of id {id} deleted")
    return {"message": "Product deleted successfully"}


# categories
#create a category
@app.get("/category")
def add_category(category:CategorySchema, db: session = Depends(get_db)):
    new_category = Category (**category.model_dump())

    db.add(new_category)
    db.commit()
    return {"message":"Category created successfully"}

@app.get("/categories")
def get_categories(db: session=Depends(get_db)):
    categories = db.query(Category).all()
    return categories
                   