from sqlalchemy import Column, Integer, String, Text, DateTime
from models.database import Base
from datetime import datetime


class MotimonoContent(Base):
    __tablename__ = 'MotimonoContent'
    id = Column(Integer, primary_key=True)
    title = Column(String(128), unique=True)
    body = Column(Text)

    def __init__(self, title=None, body=None):
        self.title = title
        self.body = body

    def __repr__(self):
        return '<Title %r>' % (self.title)