from langgraph.graph import END, StateGraph

from app.agents.planner import planner
from app.agents.state import AgentState

from app.tools.llm_tool import llm_tool
from app.tools.pdf_tool import pdf_tool
from app.tools.pdf_writer import pdf_writer
from app.tools.txt_writer import txt_writer
from app.tools.web_tool import web_tool
from app.tools.system_tool import system_tool
from app.tools.camera_tool import camera_tool
from app.tools.file_tool import file_tool
from app.tools.vision_tool import vision_tool

from app.services.assistant_state import assistant_state


# ============================================================
# Planner Node
# ============================================================

def planner_node(state: AgentState):

    selected_tool = planner.plan(state["user_input"])

    print("\n" + "=" * 60)
    print("PLANNER SELECTED:", selected_tool)
    print("=" * 60 + "\n")

    return {
        "selected_tool": selected_tool
    }


# ============================================================
# Tool Node
# ============================================================

def tool_node(state: AgentState):

    tool = state["selected_tool"]
    user_input = state["user_input"]

    # ---------------------------------------------------------
    # Summarize Uploaded PDF
    # ---------------------------------------------------------

    if tool == "summarize":

        pdf_text = pdf_tool.get_latest_pdf_text()

        if not pdf_text.strip():

            response = "No PDF has been uploaded."

        else:

            response = llm_tool.summarize(pdf_text)

    # ---------------------------------------------------------
    # Question Answering From PDF
    # ---------------------------------------------------------

    elif tool == "question_answer":

        pdf_text = pdf_tool.get_latest_pdf_text()

        if not pdf_text.strip():

            response = "No PDF has been uploaded."

        else:

            response = llm_tool.answer_from_pdf(
                pdf_text=pdf_text,
                question=user_input,
            )

    # ---------------------------------------------------------
    # General LLM
    # ---------------------------------------------------------

    elif tool == "general":

        response = llm_tool.answer_question(
            user_input
        )

    # ---------------------------------------------------------
    # Web Search
    # ---------------------------------------------------------

    elif tool == "web_search":

        web_result = web_tool.search(user_input)

        prompt = f"""
Use the web search result below to answer the user's question.

User Question:
{user_input}

Web Search Result:
{web_result}

Provide a clear, concise and accurate answer.
"""

        response = llm_tool._invoke(prompt)

    # ---------------------------------------------------------
    # Translation
    # ---------------------------------------------------------

    elif tool == "translate":

        response = llm_tool.translate(
            user_input
        )

    # ---------------------------------------------------------
    # Save Previous Response as PDF
    # ---------------------------------------------------------

    elif tool == "pdf_writer":

        last_response = assistant_state.get_last_response()

        if not last_response.strip():

            response = "No previous response available."

        else:

            path = pdf_writer.save(last_response)

            response = (
                "PDF saved successfully.\n\n"
                f"Location:\n{path}"
            )

    # ---------------------------------------------------------
    # Save Previous Response as TXT
    # ---------------------------------------------------------

    elif tool == "txt_writer":

        last_response = assistant_state.get_last_response()

        if not last_response.strip():

            response = "No previous response available."

        else:

            path = txt_writer.save(last_response)

            response = (
                "TXT saved successfully.\n\n"
                f"Location:\n{path}"
            )

    # ---------------------------------------------------------
    # Windows System Control
    # ---------------------------------------------------------

    elif tool == "system_control":

        response = system_tool.execute(
            user_input
        )

    # ---------------------------------------------------------
    # Camera Capture
    # ---------------------------------------------------------

    elif tool == "camera_reader":

        image = camera_tool.capture()

        if image:

            response = (
                "Image captured successfully."
            )

        else:

            response = (
                "Unable to access the camera."
            )

    # ---------------------------------------------------------
    # File Manager
    # ---------------------------------------------------------

    elif tool == "file_manager":

        response = file_tool.execute(
            user_input
        )

    # ---------------------------------------------------------
    # Vision AI
    # ---------------------------------------------------------

    elif tool == "vision_reader":

        response = vision_tool.describe_scene()

    # ---------------------------------------------------------
    # Unknown Tool
    # ---------------------------------------------------------

    else:

        response = "Unknown tool selected."

    print("\n" + "=" * 60)
    print("TOOL EXECUTED:", tool)
    print("=" * 60 + "\n")

    assistant_state.add_conversation(
        user=user_input,
        assistant=response,
    )

    assistant_state.set_response(
        response
    )

    assistant_state.set_tool(
        tool
    )

    return {
        "response": response
    }


# ============================================================
# Graph
# ============================================================

builder = StateGraph(AgentState)

builder.add_node(
    "planner",
    planner_node,
)

builder.add_node(
    "tool_executor",
    tool_node,
)

builder.set_entry_point(
    "planner"
)

builder.add_edge(
    "planner",
    "tool_executor",
)

builder.add_edge(
    "tool_executor",
    END,
)

graph = builder.compile()