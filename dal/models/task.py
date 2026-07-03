from .base import Base
from sqlalchemy import Column, Integer, Text, Boolean, DateTime, String
from datetime import datetime

class Task(Base):

    __tablename__ = 'Tasks'

    id = Column(Integer, primary_key=True, autoincrement=True)
    titre = Column(String(200), nullable=False)
    description = Column(Text)
    done = Column(Boolean, default = False)
    created_at = Column(DateTime, default = datetime.now())
    updated_at = Column(DateTime, default = datetime.now(), onupdate = datetime.now())