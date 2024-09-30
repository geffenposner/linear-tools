from kubiya_sdk.tools.models import Tool
from .common import COMMON_ENVIRONMENT_VARIABLES, COMMON_SECRET_VARIABLES

LINEAR_ICON_URL = "https://logowik.com/content/uploads/images/linear-app8372.logowik.com.webp"
LINEAR_API_URL = "https://api.linear.app/graphql"

class LinearApiQuery(Tool):
    def __init__(self, name, description, query, args, long_running=False, mermaid_diagram=None):
        content = f"""
        curl -X POST \\
        -H "Content-Type: application/json" \\
        -H "Authorization: ${{linear-api-key-geffen}}" \\
        --data '{{"query": "{query}"}}' \\
        {LINEAR_API_URL}
        """

        super().__init__(
            name=name,
            description=description,
            icon_url=LINEAR_ICON_URL,
            type="docker",
            image="curlimages/curl",
            content=content,
            args=args,
            env=COMMON_ENVIRONMENT_VARIABLES,
            secrets=COMMON_SECRET_VARIABLES,
            long_running=long_running,
            mermaid_diagram=mermaid_diagram
        )