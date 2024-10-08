
from kubiya_sdk.tools import Arg, Tool, FileSpec
from .base import LinearApiQuery
from kubiya_sdk.tools.registry import tool_registry
from .common import COMMON_ENVIRONMENT_VARIABLES, COMMON_SECRET_VARIABLES
from . import list_tickets
import inspect


list_tickets_inprogress = LinearApiQuery(
    name="list_tickets_inprogress",
    description="List tickets with status 'inprogress'",
    query="""
query { issues(filter: { state: { id: { eq: \"5dd19aeb-be03-41a9-9ebc-6c1a173e38c9\" } } }) { nodes { title } } }
    """,
    args=[],
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

# Register the tools
tool_registry.register("linear",list_tickets_inprogress)
tool_registry.register("linear",list_tickets_todo_python)
