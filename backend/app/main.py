# backend/app/main.py

from fastapi import FastAPI, Depends, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from . import models, schemas, crud, database, scheduler
import logging
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize the FastAPI app
app = FastAPI()

# Dependency to get DB session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.on_event("startup")
def startup_event():
    db = database.SessionLocal()
    scheduler.start_scheduler(db)
    db.close()

@app.on_event("shutdown")
def shutdown_event():
    scheduler.shutdown_scheduler()





# Define allowed origins from environment variables
origins_env = os.getenv("ALLOWED_ORIGINS", "http://localhost:3000")
origins = [origin.strip() for origin in origins_env.split(",") if origin.strip()]

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,              # List of allowed origins
    allow_credentials=True,             # Allow cookies and authorization headers
    allow_methods=["*"],                # Allow all HTTP methods
    allow_headers=["*"],                # Allow all headers
)

# Create database tables
models.Base.metadata.create_all(bind=database.engine)



# API endpoint to create or update a field mapping
@app.post("/field-mappings/", response_model=schemas.FieldMapping)
def create_or_update_field_mapping(mapping: schemas.FieldMappingCreate, db: Session = Depends(get_db)):
    return crud.create_or_update_field_mapping(db=db, mapping=mapping)

# API endpoint to get a single field mapping by api_field
@app.get("/field-mappings/{api_field}/", response_model=schemas.FieldMapping)
def get_field_mapping(api_field: str, db: Session = Depends(get_db)):
    mapping = crud.get_field_mapping(db, api_field=api_field)
    if not mapping:
        raise HTTPException(status_code=404, detail="Field mapping not found")
    return mapping

# API endpoint to get all field mappings
@app.get("/mappings/", response_model=list[schemas.FieldMapping])
def read_mappings(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    mappings = crud.get_field_mappings(db, skip=skip, limit=limit)
    return mappings

# API endpoint to create scheduler config (existing)
@app.post("/scheduler/", response_model=schemas.SchedulerConfig)
def create_scheduler_config(config: schemas.SchedulerConfigCreate, db: Session = Depends(get_db)):
    existing = crud.get_scheduler_config(db, task_name=config.task_name)
    if existing:
        raise HTTPException(status_code=400, detail="Scheduler config already exists")
    return crud.create_scheduler_config(db=db, config=config)

# API endpoint to update scheduler config (existing)
@app.put("/scheduler/{task_name}/", response_model=schemas.SchedulerConfig)
def update_scheduler(
    task_name: str, 
    enabled: bool = Query(..., description="Enable or disable the scheduler"),
    db: Session = Depends(get_db)
):
    existing = crud.get_scheduler_config(db, task_name=task_name)
    if not existing:
        raise HTTPException(status_code=404, detail="Scheduler config not found")
    try:
        updated_config = crud.update_scheduler_config(db, existing, enabled)
        if enabled:
            scheduler.scheduler.add_job(scheduler.fetch_and_store, 'interval', minutes=1, id=task_name, replace_existing=True)
            logger.info(f"Scheduler '{task_name}' enabled.")
        else:
            scheduler.scheduler.remove_job(task_name)
            logger.info(f"Scheduler '{task_name}' disabled.")
    except Exception as e:
        logger.error(f"Failed to update scheduler: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
    return updated_config

# New GET Endpoint for Single Scheduler
@app.get("/scheduler/{task_name}/", response_model=schemas.SchedulerConfig)
def get_scheduler_config(task_name: str, db: Session = Depends(get_db)):
    print(f"Received request for scheduler: {task_name}")
    config = crud.get_scheduler_config(db, task_name=task_name)
    print(f"Scheduler config: {config}")
    if not config:
        raise HTTPException(status_code=404, detail="Scheduler config not found")
    return config

# API endpoint to handle webhook (existing)
@app.post("/webhook/")
def handle_webhook(payload: dict):
    logger.info(f"Received webhook payload: {payload}")
    # Process the webhook payload as needed
    return {"status": "success"}
