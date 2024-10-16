from kubiya_sdk.tools.models import Tool
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
            image="python:3.12.6-alpine3.20",
            content=content,
            args=args,
            env=COMMON_ENVIRONMENT_VARIABLES,
            secrets=COMMON_SECRET_VARIABLES,
            long_running=long_running,
            mermaid_diagram=mermaid_diagram
        )