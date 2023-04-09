from sqlalchemy import TIMESTAMP,Boolean, Column, Integer, String, ForeignKey, DateTime, text
from database import Base
from sqlalchemy.orm import relationship

# creayting a model for the database


class Post(Base):
    __tablename__ = "userposts"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, server_default="True")
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False,  server_default=text('now()'))
    owner_id = Column(Integer, ForeignKey(
        "users.id", ondelete="CASCADE"), nullable=False)

    def __repr__(self):
        return f"Post(title={self.title}, content={self.content}, published={self.published})"
    owner = relationship("User")
# class for users


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False,  server_default=text('now()'))
