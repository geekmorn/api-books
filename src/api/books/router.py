from fastapi import APIRouter
from src.common.models import BookModel
from src.common.schemas.books import *
from src.common.utils.crd import read, create, destroy, by
from src.common.utils.exceptions import not_found

router = APIRouter(
    tags=["Books"],
    prefix="/books"
)


@router.get("/", response_model=list[Book])
async def get_all(): return await read(BookModel)


@router.get("/{id}", response_model=Book)
async def get(id: str):
    book: Book | None = await read(
        BookModel,
        by(BookModel.id, id)
    )
    if book is None:
        raise not_found()

    return book


@router.post("/", response_model=Book)
async def post(payload: BookCreate):
    return await create(BookModel, **payload.dict())


@router.delete("/", response_model=Book)
async def delete(id: str):
    book: Book | None = await read(
        BookModel,
        by(BookModel.id, id)
    )
    if book is None:
        raise not_found()

    return await destroy(book)
