import requests

class ApiClient:

    BASE_URL = "https://jsonplaceholder.typicode.com"

    def get(self, endpoint):
        response = requests.get(f"{self.BASE_URL}{endpoint}")
        return response

    def post(self, endpoint, payload):
        response = requests.post(f"{self.BASE_URL}{endpoint}", json=payload)
        return response