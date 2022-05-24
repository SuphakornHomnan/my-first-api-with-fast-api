from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(
    prefix="/user",
    tags=["User"],
    responses={404: {"message": "Not found"}}
)

userDb = [
    {
        "name": "Nice",
        "age": 23
    },
    {
        "name": "Petch",
        "age": 23
    },
    {
        "name": "Job",
        "age": 23
    }
]


class User(BaseModel):
    name: str
    age: int


@router.get("/")
async def getUsers():
    return userDb


@router.get("/{id}")
async def getUser(id: str):
    return userDb[int(id)-1]


@router.post("/")
async def createUser(user: User):
    result = user.dict()
    userDb.append(result)
    return userDb[-1]


@router.put("/{id}")
async def editUser(id: str, user: User):
    result = user.dict()
    userDb[int(id)-1].update(result)
    return result


@router.delete("/{id}")
async def deleteUser(id: str):
    user = userDb.pop(int(id)-1)
    return user
