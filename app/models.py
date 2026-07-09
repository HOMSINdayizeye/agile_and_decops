"""Pydantic request/response models for the TaskFlow API."""
from pydantic import BaseModel, ConfigDict


class Task(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    status: str


class TaskCreate(BaseModel):
    title: str


class TaskUpdate(BaseModel):
    title: str | None = None
    status: str | None = None
