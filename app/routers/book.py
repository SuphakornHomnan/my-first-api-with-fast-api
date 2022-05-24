from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(
    prefix="/book",
    tags=["Book"],
    responses={404: {"message": "Not found"}}
)

bookDb = [
    {
        "title": "The C Programming",
        "price": 720
    },
    {
        "title": "Learn Python the Hard Way",
        "price": 870
    },
    {
        "title": "JavaScript: The Definitive Guide",
        "price": 1369
    },
    {
        "title": "Python for Data Analysis",
        "price": 1394
    },
    {
        "title": "Clean Code",
        "price": 1500
    },
]


class Book(BaseModel):
    title: str
    price: float


@router.get("/")
async def getBooks():
    return bookDb


@router.get("/{id}")
async def getBook(id: str):
    return bookDb[int(id)]


@router.post("/")
async def createBook(book: Book):
    bookDb.append(book.dict())
    return bookDb[-1]


@router.put("/{id}")
async def editBook(id: str, book: Book):
    result = book.dict()
    bookDb[int(id)-1].update(result)
    return result


@router.delete("/{id}")
async def deleteBook(id: str):
    book = bookDb.pop(int(id)-1)
    return book
