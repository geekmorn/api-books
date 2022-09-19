from fastapi import APIRouter
from src.common.models import CategoryModel
from src.common.schemas.categories import *
from src.common.utils.crd import read, create, destroy, by
from src.common.utils.exceptions import not_found

router = APIRouter(
    tags=["Categories"],
    prefix="/categories"
)


@router.get("/", response_model=list[Category])
async def get_all(): return await read(CategoryModel)


@router.get("/{id}", response_model=Category)
async def get(id: str):
    category: Category | None = await read(
        CategoryModel,
        by(CategoryModel.id, id)
    )
    if category is None:
        raise not_found()

    return category


@router.post("/", response_model=Category, status_code=201)
async def post(payload: CategoryCreate):
    return await create(CategoryModel, **payload.dict())


@router.delete("/", response_model=Category)
async def delete(id: str):
    category: Category | None = await read(
        CategoryModel,
        by(CategoryModel.id, id)
    )
    if category is None:
        raise not_found()

    return await destroy(category)
