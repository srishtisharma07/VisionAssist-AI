from typing import TypedDict


class AgentState(TypedDict):
    user_input: str
    selected_tool: str
    response: str