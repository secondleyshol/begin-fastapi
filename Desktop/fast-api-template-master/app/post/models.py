from sqlalchemy import Column, String

from app.repository.base import Base


class Post(Base):
    title = Column(String)
    content = Column(String)



