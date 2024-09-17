# backend/app/scheduler.py

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
import requests
import logging

logger = logging.getLogger(__name__)

scheduler = BackgroundScheduler()

def fetch_and_store():
    logger.info("Fetching data from external API...")
    # Example: Fetch data from a dummy API
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    if response.status_code == 200:
        data = response.json()
        # Here you would map and store data to the database
        logger.info(f"Fetched {len(data)} records.")
    else:
        logger.error("Failed to fetch data.")

def start_scheduler(db_session):
    
    scheduler.add_job(fetch_and_store, IntervalTrigger(minutes=1), id="fetch_data", replace_existing=True)
    scheduler.start()
    logger.info("Scheduler started.")

def shutdown_scheduler():
    scheduler.shutdown()
    logger.info("Scheduler shut down.")
