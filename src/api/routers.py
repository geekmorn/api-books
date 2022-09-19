from fastapi import APIRouter
from ..common.config.settings import settings
from .categories import category_router
from .books import book_router


api_router = APIRouter(
    prefix=settings.ROUTE_PREFIX
)

ROUTERS = [
    category_router,
    book_router
]


for router in ROUTERS:
    api_router.include_router(router)
