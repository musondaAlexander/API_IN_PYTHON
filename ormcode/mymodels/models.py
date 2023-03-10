from sqlalchemy import Boolean, Column, Integer, String, ForeignKey, DateTime
from database import Base

# creayting a model for the database


class Post(Base):
    __tablename__ = "userposts"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, default=True)

    def __repr__(self):
        return f"Post(title={self.title}, content={self.content}, published={self.published})"
