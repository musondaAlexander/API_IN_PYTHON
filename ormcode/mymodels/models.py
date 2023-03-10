from sqlalchemy import TIMESTAMP, Boolean, Column, Integer, String, ForeignKey, DateTime, text
from database import Base

# creayting a model for the database


class Post(Base):
    __tablename__ = "userposts"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, server_default="True")
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False,  server_default=text('now()'))

    def __repr__(self):
        return f"Post(title={self.title}, content={self.content}, published={self.published})"
