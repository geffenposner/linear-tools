from kubiya_sdk.tools import Arg
from .base import LinearApiTool
from kubiya_sdk.tools.registry import tool_registry

list_tickets_todo = LinearApiTool(
    name="list_tickets_todo",
    description="List tickets with status 'todo'",
    query="""
    {
      issues(filter: { state: { id: "53c71e8a-8ccb-4ee5-99e6-53a4056c6072" } }) {
        nodes {
          id
          title
          description
        }
      }
    }
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
        Arg(name="title", type="string", description="Title of the issue"),
        Arg(name="description", type="string", description="Description of the issue"),
        Arg(name="team_id", type="string", description="ID of the team to assign the issue to"),
    ],
)

# Register the tools
tool_registry.register(list_tickets_todo)
tool_registry.register(create_issue)
