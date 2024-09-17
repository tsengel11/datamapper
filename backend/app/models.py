# backend/app/models.py

from sqlalchemy import Column, Integer, String, Boolean
from .database import Base

class FieldMapping(Base):
    __tablename__ = "field_mappings"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    api_field = Column(String, unique=True, index=True)
    db_field = Column(String, unique=True, index=True)

class SchedulerConfig(Base):
    __tablename__ = "scheduler_config"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    task_name = Column(String, unique=True, index=True)
    enabled = Column(Boolean, default=False)
