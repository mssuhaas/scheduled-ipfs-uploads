import requests

class APIHandler:
    def __init__(self, api_url):
        self.api_url = api_url

    def send_data(self, data):
        # Only send data if it's not empty
        if not data:
            return {"status": "error", "message": "No data to upload"}
        response = requests.post(f"{self.api_url}/upload_data/", json={"data": data})
        return response.json()
