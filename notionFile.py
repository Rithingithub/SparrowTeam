import json
import requests

notion_token = '<API_TOKEN>'
DBid = '3c35a8a4641e441c9fafff1dca38cd26'

headers = {
      "Notion-Version": "2021-05-13",
      "Content-Type": "application/json",
      "Authorization": "Bearer " + notion_token
    }
    #self.base_url = "https://api.notion.com/v1"
 
def readDB(DBid):
    readUrl = f"https://api.notion.com/v1/databases/{DBid}/query"

    res = requests.request("POST", readUrl, headers=headers)
    data = res.json()
    print(res.status_code)
