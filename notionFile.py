import json
import requests

notion_token = '<API_TOKEN>'


class Notion:

  def __init__(self, notion_token):
    self.headers = {
      'Notion-Version': '2021-05-13',
      'Authorization': 'Bearer ' + notion_token
    }
    self.base_url = "https://api.notion.com/v1"