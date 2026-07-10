from langgraph.graph import END, StateGraph

from app.agents.router import router
from app.agents.state import AgentState
from app.agents.tools import gemini_tool


def router_node(state: AgentState):

    tool = router.route(state["user_input"])

    return {
        "selected_tool": tool
    }


def tool_node(state: AgentState):

    tool = state["selected_tool"]

    user_input = state["user_input"]

    if tool == "summarize":

        response = gemini_tool.summarize(user_input)

    elif tool == "explain":

        response = gemini_tool.explain(user_input)

    elif tool == "translate":

        response = gemini_tool.translate(user_input)

    elif tool == "question_answer":

        response = gemini_tool.answer_question(user_input)

    elif tool == "pdf_writer":

        response = "PDF Writer Tool will be implemented soon."

    elif tool == "txt_writer":

        response = "TXT Writer Tool will be implemented soon."

    else:

        response = "Unknown tool."

    return {
        "response": response
    }


builder = StateGraph(AgentState)

builder.add_node("router", router_node)
builder.add_node("tool_executor", tool_node)

builder.set_entry_point("router")

builder.add_edge("router", "tool_executor")
builder.add_edge("tool_executor", END)

graph = builder.compile()