from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class Worker(Base):
    __tablename__ = "workers"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    name = Column(String, unique=True, index=True)

    tractors = relationship("Tractor", back_populates="owner")


class Tractor(Base):
    __tablename__ = "tractor"

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String, index=True)
    year = Column(String, index=True)
    worker_id = Column(Integer, ForeignKey("workers.id"))

    owner = relationship("Worker", back_populates="tractors")
