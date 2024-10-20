import os
import requests
import argparse

print(os.environ)
linear_api_key = os.environ['linear_api_key_geffen']

def list_tickets_dynamic_python(stateID: str):
    query = {
  "query": f'query {{ issues(filter: {{ state: {{ id: {{ eq: "{stateID}" }} }} }}) {{ nodes {{ title }} }} }}'
}
    print(linear_api_key)

    response = requests.post(
        "https://api.linear.app/graphql",
        headers={"Authorization": linear_api_key},
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