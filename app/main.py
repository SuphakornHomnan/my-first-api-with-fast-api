from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from .routers import book, user, file
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(book.router)
app.include_router(user.router)
app.include_router(file.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
