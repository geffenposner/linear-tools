
from kubiya_sdk.tools import Arg, Tool, FileSpec
from .base import LinearApiTool
from kubiya_sdk.tools.registry import tool_registry
from .common import COMMON_ENVIRONMENT_VARIABLES, COMMON_SECRET_VARIABLES
from . import list_tickets
import inspect

list_tickets_todo = LinearApiTool(
    name="list_tickets_todo",
    description="List tickets with status 'todo'",
    query="""
query { issues(filter: { state: { id: { eq: \"53c71e8a-8ccb-4ee5-99e6-53a4056c6072\" } } }) { nodes { title } } }
    """,
    args=[],
)

# Example of a new tool with input
create_issue = LinearApiTool(
    name="create_issue",
    description="Create a new issue",
    query="""
    mutation {
      issueCreate(input: {
        title: "{{.title}}",
        description: "{{.description}}",
        teamId: "{{.team_id}}"
      }) {
        success
        issue {
          id
          title
          description
        }
      }
    }
    """,
    args=[
        Arg(name="title", type="str", description="Title of the issue"),
        Arg(name="description", type="str", description="Description of the issue"),
        Arg(name="team_id", type="str", description="ID of the team to assign the issue to"),
    ],
)

list_tickets_todo_python = Tool(
    name="list_tickets_todo_python",
    description="List tickets with status 'todo' using python",
    type="docker",
    image="python:3.12",
    env=COMMON_ENVIRONMENT_VARIABLES,
    secrets=COMMON_SECRET_VARIABLES,
    content="""
pip install requests

python /tmp/list_tickets.py
""",
    files=[
        FileSpec(destination="/tmp/list_tickets.py", content=inspect.getsource(list_tickets))
    ],
)

# Register the tools
tool_registry.register("linear",list_tickets_todo)
tool_registry.register("linear",create_issue)
tool_registry.register("linear",list_tickets_todo_python)
