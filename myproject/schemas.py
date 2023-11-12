from __future__ import annotations
from typing import Optional

from pydantic import BaseModel


class TractorBase(BaseModel):
    title: str
    description: str | None = None


class TractorCreate(TractorBase):
    pass


class Tractor(TractorBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class WorkerBase(BaseModel):
    email: str


class WorkerCreate(WorkerBase):
    password: str


class Worker(WorkerBase):
    id: int
    is_active: Optional[bool]

    tractors: list[Tractor] = []

    class Config:
        orm_mode = True
