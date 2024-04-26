import requests
import json

class RestClient:
  def __init__(self, base_url):
    self.base_url = base_url
  
  def get(self, resource):
    url = f"{self.base_url}/{resource}"
    response = requests.get(url)

    return json.loads(response.content)

  def post(self, resource, params):
    url = f"{self.base_url}/{resource}"
    response = requests.post(url, json=params)

    return json.loads(response.content)