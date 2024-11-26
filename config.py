import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    IPFS_GATEWAY = os.getenv("IPFS_GATEWAY")

