import json
import requests

notion_token = '<API_KEY>'
DBid = '<ID>'


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


def createPage(DBid, headers):
    createUrl = 'https://api.notion.com/v1/pages'

    newPageData = {
        "parent": {"database_id": DBid},
        "properties": {
            "Description": {
                "title": [
                    {
                        "text": {
                            "content": "Review"
                        }
                    }
                ]
            },
            "Value": {
                "rich_text": [
                    {
                        "text": {
                            "content": "Amazing"
                        }
                    }
                ]
            },
            "Status": {
                "rich_text": [
                    {
                        "text": {
                            "content": "Active"
                        }
                    }
                ]
            }
        }
    }

    data = json.dumps(newPageData)

    res = requests.request("POST", createUrl, headers=headers, data=data)
    print(res.text)

def updatePage(padeId, headers):
    updateUrl = f"https://api.notion.com/v1/pages/{pageId}"

    updateData = {
        "properties": {
            "Value": {
                "rich_text": [
                    {
                        "text": {
                            "content": "Pretty Good"
                        }
                    }
                ]
            }        
        }
    }

    data = json.dumps(updateData)

    response = requests.request("PATCH", updateUrl, headers=headers, data=data)
    print(response.text)
