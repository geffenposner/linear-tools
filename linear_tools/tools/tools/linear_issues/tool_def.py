from . import list_tickets_dynamic

import inspect


from kubiya_sdk.tools.models import Tool, Arg, FileSpec
from kubiya_sdk.tools.registry import tool_registry

from .common import COMMON_ENVIRONMENT_VARIABLES, COMMON_SECRET_VARIABLES

LINEAR_ICON_URL = "https://logowik.com/content/uploads/images/linear-app8372.logowik.com.webp"

list_tickets_by_workflow_state_id = Tool(
    name="list_tickets_by_workflow_state_id",
    icon_url=LINEAR_ICON_URL,
    type="docker",
    image="python:3.12",
    description="lists Linear tickets with workflow state ID {stateID}",
    args=[Arg(name="stateID", description="workflow stateID of the tickets you want to see", required=True)],
    content="""
curl -LsSf https://astral.sh/uv/install.sh | sh > /dev/null 2>&1
. $HOME/.cargo/env

uv venv > /dev/null 2>&1
. .venv/bin/activate > /dev/null 2>&1

uv pip install requests > /dev/null 2>&1

python /tmp/list_tickets_dynamic.py "{{ .stateID }}"
""",
    env=COMMON_ENVIRONMENT_VARIABLES,
    secrets=COMMON_SECRET_VARIABLES,
    with_files=[
        FileSpec(
            destination="/tmp/list_tickets_dynamic.py",
            content=inspect.getsource(list_tickets_dynamic),
        ),
    ],
)


tool_registry.register("linear", list_tickets_by_workflow_state_id)

