# importing fastapi
from datetime import datetime, time, timedelta
from enum import Enum
from uuid import UUID
from fastapi import (
    FastAPI,
    Depends,
    Query,
    Path,
    Body,
    Cookie,
    Header,
    HTTPException,
    Request,
    status
)
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse, PlainTextResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from typing import Optional
from pydantic import BaseModel, Field, HttpUrl
# from passlib.context import CryptContext
# from jose import jwt, JWTError
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
# instantiating the app
app = FastAPI()

# Setting route to communicate with the app
# the syntax below is decorator
# here '/' --means base url(localhost here)


@app.get("/")
async def index():
    return {"message": "Hello World"}


# path parameters
@app.get("/users")
async def item_request():
    return {"message": "users_request"}


# look into which route to use first
@app.get("/users/me")
async def get_current_user():
    return {"Message": "This is current User"}


@app.get("/users/{user_id}")
async def get_user(user_id: str):
    return {"User_id": user_id}


class FoodEnum(str, Enum):
    fruits = "fruits"
    vegetables = "vegetables"
    dairy = "dairy"


@app.get("/foods/{food_name}")
async def get_food(food_name: FoodEnum):
    if food_name == FoodEnum.vegetables:
        return {"Food_name": food_name, "message": "you are healthy"}

    if food_name.value == "fruits":
        return {
            "Food_name": food_name,
            "message": "you are still healthy but like sweet things"
        }
    return {"food_name": food_name, "message": "I like chocolate milk"}


# creating fake database to understand query parameters:
fake_db = [{"item_name": "Foo"}, {"item_name": "Box"}, {"item_name": "Bat"}, {"item_name": "pen"}]


# if we do not define item_id as int it would give string to us
@app.get("/items")
async def list_items(skip: int = 0, limit: int = 10):
    return fake_db[skip: skip + limit]


# Optional Query Parameter
# instead of optional we can use q: str | None = None
@app.get("/items/{item_id}")
async def get_item(item_id: str, q: Optional[str] = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}


# Boolean conversion here the default value for short is False
@app.get("/list/{list_id}")
async def read_list(list_id: str, q: str | None = None, short: bool = False):
    item = {"list_id": list_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update({"description": "This is an amazing item that has a long description"})
    return item


# Multiple path and query parameters:
@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(user_id: int, item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update({"description": "This is an amazing item that has a long description"})
    return item


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


@app.post("/item")
async def create_item(item: Item):
    item_dict = item.model_dump()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict


# Request body + path + query parameters
@app.put("/item/{item_id}")
async def create_item(item_id: int, item: Item, q: str | None = None):
    result = {"item_id": item_id, **item.model_dump()}
    if q:
        result.update({"q": q})
    return result


@app.get("/list_reading")
async def read_items_list(q: list[str] | None = Query(None)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


# Here in regex which ever regular expression is given should only be given as query
@app.get("/reading")
async def read_items(q: str = Query(..., min_length=3, max_length=10)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


# @app.get("/items")
# async def read_items(q: Annotated[str | None, Query(max_length=50)] = None):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results


@app.get("/items_hidden")
async def hidden_query_route(hidden_query: str | None = Query(None, include_in_schema=False)):
    if hidden_query:
        return {"Hidden_Query": "hidde_query"}
    return {"Hidden_Query": "Not_Found"}


@app.get("/items_validation/{item_id}")
async def read_items_validation(
        *,
        item_id: int = Path(..., title="The ID of the item to get", gt=10, le=100),
        q: str = "hello",
        size: float = Query(..., gt=0, lt=7.75)
):
    results = {"item_id": item_id, "size": size}
    if q:
        results.update({"q": q})
    return results


"""
Part 7-> body parameters
"""

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


class User(BaseModel):
    username: str
    full_name: str | None = None


@app.put("/items/{item_id}")
async def update_item(
        *,
        item_id: int = Path(..., title="The ID of Item", ge=0, le=100),
        q: str | None = None,
        item: Item | None = None,
        user: User | None = None,
        importance: int = Body(...)
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    if item:
        results.update({"item": item})
    if user:
        results.update({"user": user})
    if importance:
        results.update({"importance": importance})
    return results
"""
Part 8-> body field
"""


class Item(BaseModel):
    name: str
    description: str = Field(
        ..., title="This is description", max_length=300
    )
    price: float = Field(..., gt=0, description="Price of item should be greater than 0")
    tax: float


@app.put("/item/{item_id}")
async def update_item(item_id: int, item: Item = Body(..., embed=True)):
    results = {"item_id": item_id, "item": item}
    return results
"""
Part 9-> body NESTED Models
"""


class Image(BaseModel):
    name: str
    url: HttpUrl


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[int] = set()
    image: list[Image] | None = None


class Offer(BaseModel):
    name: str
    description: str | None = None
    price: float
    item: list[Item]


@app.put("/item/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results


@app.post("/offers")
async def create_offer(offer: Offer = Body(..., embed=True)):
    return offer


@app.post("/images/multiple")
async def upload_images(images: list[Image] = Body(..., embed=True)):
    return images
"""
Part 10-> Declare Request Example Data
"""


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

    # class Config:
    #     schema_extra = {
    #         'example': {
    #             "name": "Foo",
    #             "description": "A basic Item",
    #             "price": 10.50,
    #             "tax": 2.25
    #         }
    #     }


@app.put("/item/{item_id}")
async def update_item(
        item_id: int,
        item: Item = Body(..., example={"name": "Foo", "description": "A basic Item", "price": 10.60, "tax": 2.25})):
    results = {"item_id": item_id, "item": item}
    return results


# Extra Data Types: UUID
@app.put("/item/{item_id}")
async def read_item(
        item_id: UUID,
        start_date: datetime | None = Body(None),
        end_date: datetime | None = Body(None),
        repeat_at: time | None = Body(None),
        process_after: timedelta | None = Body(None)
):
    start_process = start_date + process_after
    duration = end_date - start_process
    return {"item_id": item_id, "start_date": start_date, "end_date": end_date, "repeat_at": repeat_at,
            "process_after": process_after, "start_process": start_process, "duration": duration
            }


@app.get("/items")
async def read_item(cookie_id: str | None = Cookie(None)):
    return {"Cookie_id": cookie_id}
"""
Part 11-> Response Model
"""


class Item(BaseModel):
    name: str
    description: str
    price: float
    tax: float
    tag: list[str] = []


@app.post("/items", response_model=Item)
async def create_item(item: Item):
    return item
"""
Part 19-> Handling error
"""


items = {"foo": "The foo Wrestler"}


@app.get("/items/{item_id}")
async def read_item(item_id: str):
    if item_id not in items:
        raise HTTPException(
            status_code=404,
            detail="Item not found",
            headers={"X-Error": "There goes my error"})
    return {"item": items[item_id]}


class UnicornException(Exception):
    def __init__(self, name: str):
        self.name = name


@app.exception_handler(UnicornException)
async def unicorn_exception_handler(request: Request, exc: UnicornException):
    return JSONResponse(
        status_code=418,
        content={"message": f"Oops! {exc.name} did something. There goes a rainbow..."}
    )


@app.get("/unicorns/{name}")
async def read_unicorns(name: str):
    if name == "yolo":
        raise UnicornException(name=name)
    return {"unicorn_name": name}


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return PlainTextResponse(str(exc), status_code=400)


@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    return PlainTextResponse(str(exc.detail), status_code=exc.status_code)


@app.get("/validation_items/{item_id}")
async def read_validation_items(item_id: int):
    if item_id == 3:
        raise HTTPException(status_code=418, detail="No I don't like 3.")
    return{"item_id": item_id}


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail": exc.errors(), "body": exc.body})
    )


class Item(BaseModel):
    title: str
    size: int


@app.post("/items/")
async def create_item(item: Item):
    return item
"""
Part 20-> Path Operation Configuration
"""


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str] = set()


class Tags(Enum):
    items = "items"
    users = "users"


@app.post(
    "/items/",
    response_model=Item,
    status_code=status.HTTP_201_CREATED,
    tags=[Tags.items],
    description="Create an item with all information"
)
async def create_item(item: Item):
    return item


@app.get("/items/", tags=[Tags.items])
async def read_items():
    return [{"name": "Foo", "price": 45}]


@app.get("/users/", tags=[Tags.users])
async def read_users():
    return [{"username": "Phoebe"}]
"""
Part 21-> JSON COMPATIBLE ENCODER AND BODY UPDATES
"""


class Item(BaseModel):
    name: str | None = None
    description: str | None = None
    price: float | None = None
    tax: float = 10.5
    tags: list[str] = []


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bar", "price": 62, "tax": 12.3},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10, "tags": []},
}


@app.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: str):
    return items.get(item_id)


@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: str, item: Item):
    update_item_encoded = jsonable_encoder(item)
    items[item_id] = update_item_encoded
    return update_item_encoded


@app.patch("/items/{item_id}", response_model=Item)
def patch_item(item_id: str, item: Item):
    stored_item_data = items.get(item_id)
    if stored_item_data is not None:
        stored_item_model = Item(**stored_item_data)
    else:
        stored_item_model = Item()
    update_data = item.model_dump()
    print(update_data)
    updated_item = stored_item_model.model_copy(update=update_data)
    items[item_id] = jsonable_encoder(updated_item)
    print(items[item_id])
    return updated_item
"""
Part 22-> Dependencies
"""


async def hello():
    return "world"


async def common_parameters(q: str | None = None, skip: int = 0, limit: int = 100, blah: str = Depends(hello)):
    return {"q": q, "skip": skip, "limit": limit}


@app.get("/items/")
async def read_items(commons: dict = Depends(common_parameters)):
    return commons


@app.get("/users/")
async def read_user(commons: dict = Depends(common_parameters)):
    return commons
"""
Part 25-> Dependencies in path operation, decorators, global dependencies
"""


async def verify_token(x_token: str = Header(...)):
    if x_token != "fake-code":
        raise HTTPException(status_code=400, detail="x-token invalid")
    return 'hello'


@app.get("/items")
async def read_items(blah: str = Depends(verify_token)):
    print(blah)
    return[{"item": "Foo"}, {"item": "bar"}]
"""
Part 26-> Security, Sessions, first steps
"""
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


fake_users_db = {
    "jhondoe": dict(
        username="john",
        full_name="john Doe",
        email="johndoe@gmail.com",
        hashed_password="fakehasedsecret1",
        disabled=False
    ),
    "alice": dict(
        username="alice",
        full_name="Alice Wander",
        email="alicewander@gmail.com",
        hashed_password="fakehasedsecret2",
        disabled=True
    )
}


def fake_hash_password(password: str):
    return f"fakehashed{password}"


class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disable: bool | None = None


class UserInDB(User):
    hashed_password: str


def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)


def fake_decode_token(token):
    return get_user(fake_users_db, token)


async def get_current_user(token: str = Depends(oauth2_scheme)):
    user = fake_decode_token(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"www-Authenticate": "Bearer"}
        )
    return user


async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.disable:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user_dict = fake_users_db.get(form_data.username)
    if not user_dict:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    user = UserInDB(**user_dict)
    hashed_password = fake_hash_password(form_data.password)
    if not hashed_password == user.hashed_password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    return {"access_token": user.username, "token_type": "bearer"}


@app.get("/users/me")
async def get_me(current_user: User = Depends(get_current_active_user)):
    return current_user


@app.get("/items/")
async def read_items(token: str = Depends(oauth2_scheme)):
    return {"token": token}


