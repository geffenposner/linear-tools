import os
import requests


def list_tickets_todo_python():
    query = {
  "query": "query { issues(filter: { state: { id: { eq: \"53c71e8a-8ccb-4ee5-99e6-53a4056c6072\" } } }) { nodes { title } } }"
}

    response = requests.post(
        "https://api.linear.app/graphql",
        headers={"Authorization": f"{os.getenv('linear-api-key-geffen')}"},
        json=query,
    )
    return response.json()

if __name__ == "__main__":
    print(list_tickets_todo_python())