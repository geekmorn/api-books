from pydantic import BaseModel


class CategoryCreate(BaseModel):
    name: str


class Category(BaseModel):
    id: str
    name: str

    class Config:
        orm_mode = True
