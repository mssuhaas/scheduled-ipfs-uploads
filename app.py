from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from data_collector import DataCollector
from ipfs_handler import IPFSHandler
from config import Config
import atexit
from apscheduler.schedulers.background import BackgroundScheduler

app = FastAPI()

class DataRequest(BaseModel):
    data: dict

ipfs_handler = IPFSHandler(Config.IPFS_GATEWAY)
data_collector = DataCollector(ipfs_handler)

scheduler = BackgroundScheduler()

@app.on_event("startup")
def start_scheduler():
    scheduler.add_job(data_collector.upload_data, 'interval', minutes=10)
    scheduler.start()

@app.on_event("shutdown")
def stop_scheduler():
    scheduler.shutdown()

atexit.register(stop_scheduler)

@app.post("/upload_data/")
async def upload_data(request: DataRequest):
    try:
        data = request.data
        if not data:
            return {"status": "skipped", "message": "No data provided to upload"}

        data_collector.store_data(data)
        return {"status": "success", "message": "Data stored, upload will be attempted in 10 minutes (or at the next scheduled interval)."}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
async def read_root():
    return {"message": "IPFS Data Upload API is running"}

