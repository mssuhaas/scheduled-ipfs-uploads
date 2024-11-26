import requests

class IPFSHandler:
    def __init__(self, ipfs_gateway):
        self.ipfs_gateway = ipfs_gateway

    def store_data(self, text_data):
        files = {
            "file": ("data.txt", text_data)
        }
        try:
            response = requests.post(f"{self.ipfs_gateway}/api/v0/add", files=files, timeout=10)
            if response.status_code == 200:
                ipfs_hash = response.json()["Hash"]
                return ipfs_hash
        except requests.exceptions.RequestException as e:
            print(f"Error connecting to IPFS: {e}")
        return None

