# backend/app/crud.py

from sqlalchemy.orm import Session
from . import models, schemas
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError

def get_field_mapping_by_api_field(db: Session, api_field: str):
    return db.query(models.FieldMapping).filter(models.FieldMapping.api_field == api_field).first()

def create_or_update_field_mapping(db: Session, mapping: schemas.FieldMappingCreate):
    existing_mapping = get_field_mapping_by_api_field(db, api_field=mapping.api_field)
    if existing_mapping:
        # Update existing mapping's db_field
        existing_mapping.db_field = mapping.db_field
        try:
            db.commit()
            db.refresh(existing_mapping)
            return existing_mapping
        except IntegrityError:
            db.rollback()
            raise HTTPException(status_code=400, detail="DB field already exists for another API field.")
    else:
        # Create new mapping
        new_mapping = models.FieldMapping(api_field=mapping.api_field, db_field=mapping.db_field)
        db.add(new_mapping)
        try:
            db.commit()
            db.refresh(new_mapping)
            return new_mapping
        except IntegrityError:
            db.rollback()
            raise HTTPException(status_code=400, detail="API field or DB field already exists.")
        
def get_scheduler_config(db: Session, task_name: str):
    print(f"Received request for scheduler: {task_name}")
    return db.query(models.SchedulerConfig).filter(models.SchedulerConfig.task_name == task_name).first()

def create_scheduler_config(db: Session, config: schemas.SchedulerConfigCreate):
    db_config = models.SchedulerConfig(task_name=config.task_name, enabled=config.enabled)
    db.add(db_config)
    try:
        db.commit()
        db.refresh(db_config)
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Scheduler config already exists.")
    return db_config

def update_scheduler_config(db: Session, config: models.SchedulerConfig, enabled: bool):
    config.enabled = enabled
    db.commit()
    db.refresh(config)
    return config

def get_field_mapping(db: Session, api_field: str):
    return db.query(models.FieldMapping).filter(models.FieldMapping.api_field == api_field).first()

def create_field_mapping(db: Session, mapping: schemas.FieldMappingCreate):
    db_mapping = models.FieldMapping(api_field=mapping.api_field, db_field=mapping.db_field)
    db.add(db_mapping)
    try:
        db.commit()
        db.refresh(db_mapping)
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="API field or DB field already exists.")
    return db_mapping

def get_field_mappings(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.FieldMapping).offset(skip).limit(limit).all()
