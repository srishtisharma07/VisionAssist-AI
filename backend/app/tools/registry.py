from app.tools.system_tool import system_tool
from app.tools.web_tool import web_tool


class ToolRegistry:

    def __init__(self):

        self.tools = {
            "system_control": system_tool,
            "web_search": web_tool,
        }

    def get(self, tool_name: str):

        return self.tools.get(tool_name)

    def execute(self, tool_name: str, command: str):

        tool = self.get(tool_name)

        if tool is None:
            return None

        return tool.execute(command)


tool_registry = ToolRegistry()