import os
import requests
import argparse

def list_tickets_dynamic_python(stateID: str):
    query = {
  "query": f'query {{ issues(filter: {{ state: {{ id: {{ eq: "{stateID}" }} }} }}) {{ nodes {{ title }} }} }}'
}

    response = requests.post(
        "https://api.linear.app/graphql",
        headers={"Authorization": os.getenv('linear-api-key-geffen')},
        json=query,
    )
    return response.json()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Query linear for tickets with state ID{stateID}!")
    parser.add_argument("stateID", help="Workflow State ID of the tickets you want to see")

    # Parse command-line arguments
    args = parser.parse_args()

    # Get coordinates for the given city ???
    stateID = args.stateID

    print(list_tickets_dynamic_python(stateID))