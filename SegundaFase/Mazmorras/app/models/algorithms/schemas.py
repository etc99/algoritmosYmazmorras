from sqlalchemy import Column, String, Integer
from app.schemas import Base

class Algorithm(Base):
    __tablename__ = 'algorithms'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
