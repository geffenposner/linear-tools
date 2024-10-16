from . import list_tickets_dynamic, list_tickets
import inspect
from kubiya_sdk.tools.models import Tool, Arg, FileSpec
from kubiya_sdk.tools.registry import tool_registry
from .common import COMMON_ENVIRONMENT_VARIABLES, COMMON_SECRET_VARIABLES

LINEAR_ICON_URL = "https://logowik.com/content/uploads/images/linear-app8372.logowik.com.webp"
LINEAR_API_URL = "https://api.linear.app/graphql"

class LinearApiQuery(Tool):
    def __init__(self, name, description, content, args, long_running=False, mermaid_diagram=None):

        super().__init__(
            name=name,
            description=description,
            icon_url=LINEAR_ICON_URL,
            type="docker",
            image="python:3.12",
            content=content,
            args=args,
            env=COMMON_ENVIRONMENT_VARIABLES,
            secrets=COMMON_SECRET_VARIABLES,
            long_running=long_running,
            mermaid_diagram=mermaid_diagram
        )


list_tickets_by_state = Tool(
    name="list_tickets_by_workflow_state",
    type="docker",
    image="python:3.12",
    description="lists Linear tickets with workflow state ID {stateID}",
    args=[Arg(name="stateID", description="workflow stateID of the tickets you want to see", required=True)],
    content="""
python /tmp/list_tickets_dynamic.py "{{ .stateID }}"
""",
    with_files=[
        FileSpec(
            destination="/tmp/list_tickets_dynamic.py",
            content=inspect.getsource(list_tickets_dynamic),
        ),
    ],
)


list_tickets_todo_python = Tool(
    name="list_tickets_todo_python",
    description="List tickets with status 'todo' using python",
    type="docker",
    image="python:3.12.6-alpine3.20",
    env=["COMMON_ENVIRONMENT_VARIABLES"],
    secrets=COMMON_SECRET_VARIABLES,
    content="""
pip install requests

python /tmp/list_tickets.py
""",
    with_files=[
        FileSpec(destination="/tmp/list_tickets.py", content=inspect.getsource(list_tickets))
    ],
)


#Register the tools
tool_registry.register("linear", list_tickets_by_state)
tool_registry.register("linear",list_tickets_todo_python)