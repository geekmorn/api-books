from sqlalchemy import Column, String
from ..config.database import Base
from sqlalchemy.orm import relationship


class CategoryModel(Base):
    __tablename__ = "category"

    id = Column(String, primary_key=True)
    name = Column(String)

    book = relationship("BookModel", back_populates="category")
