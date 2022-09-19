from pydantic import BaseModel


class BookCreate(BaseModel):
    name: str
    author: str
    category_id: str


class Book(BaseModel):
    id: str
    name: str
    author: str
    category_id: str

    class Config:
        orm_mode = True
