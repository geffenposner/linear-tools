
from kubiya_sdk.tools import Arg, Tool, FileSpec
from .base import LinearApiQuery
from kubiya_sdk.tools.registry import tool_registry
from .common import COMMON_ENVIRONMENT_VARIABLES, COMMON_SECRET_VARIABLES



# Example of a new tool with input
create_issue = LinearApiQuery(
    name="create_issue",
    description="Create a new issue",
    content="""
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



# Register the tools
tool_registry.register("linear",create_issue)