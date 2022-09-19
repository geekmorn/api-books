from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from ..config.database import Base


class BookModel(Base):
    __tablename__ = "book"

    id = Column(String, primary_key=True)
    name = Column(String)
    author = Column(String)
    category_id = Column(ForeignKey("category.id"))

    category = relationship("CategoryModel", back_populates="book")
