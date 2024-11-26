from datetime import datetime
from ipfs_handler import IPFSHandler
from utils import convert_data_to_text

class DataCollector:
    def __init__(self, ipfs_handler):
        self.ipfs_handler = ipfs_handler
        self.stored_data = []  # Initialize as an empty list

    def collect_data(self):
        data = {
            "timestamp": str(datetime.now()),
            "temperature": 22.5,
            "humidity": 60
        }
        return data

    def store_data(self, data):
        self.stored_data.append(data)
        print(f"Data stored: {data}")

    def upload_data(self):
        if not self.stored_data:
            print("No data to upload.")
            return

        text_data = convert_data_to_text(self.stored_data)
        ipfs_hash = self.ipfs_handler.store_data(text_data)

        if ipfs_hash:
            print(f"Data uploaded to IPFS with CID: {ipfs_hash}")
            self.stored_data.clear()  # Clear only after successful upload
        else:
            print("Failed to upload data to IPFS. Data not cleared.")

