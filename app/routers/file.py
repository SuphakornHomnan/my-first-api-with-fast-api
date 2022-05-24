from fastapi import File, UploadFile, APIRouter
from typing import List

router = APIRouter(
    prefix="/file",
    tags=["File"],
    responses={404: {"message": "Not found"}}
)


@router.post("/")
async def uploagFile(file: UploadFile = File(...)):
    size = await file.read()
    return {"File Name": file.filename, "size": len(size)}


@router.post("/multi")
async def uploadMultiFile(files: List[UploadFile] = File(...)):
    file = [
        {
            "File Name": file.filename,
            "Size": len(await file.read())
        } for file in files]
    return file
