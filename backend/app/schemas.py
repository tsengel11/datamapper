# backend/app/schemas.py

from pydantic import BaseModel

class FieldMappingBase(BaseModel):
    api_field: str
    db_field: str

class FieldMappingCreate(FieldMappingBase):
    pass

class FieldMapping(FieldMappingBase):
    id: int

    class Config:
        orm_mode = True

class SchedulerConfigBase(BaseModel):
    task_name: str
    enabled: bool

class SchedulerConfigCreate(SchedulerConfigBase):
    pass

class SchedulerConfig(SchedulerConfigBase):
    id: int

    class Config:
        orm_mode = True
