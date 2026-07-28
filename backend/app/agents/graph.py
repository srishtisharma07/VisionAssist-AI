from langgraph.graph import END, StateGraph
import traceback

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
from app.tools.document_reader import document_reader

from app.services.assistant_state import assistant_state


# ============================================================
# Planner Node
# ============================================================

ALLOWED_TOOLS = {
    "general",
    "question_answer",
    "summarize",
    "translate",
    "pdf_writer",
    "txt_writer",
    "web_search",
    "system_control",
    "camera_reader",
    "file_manager",
    "vision_reader",
    "document_chat",
}


def planner_node(state: AgentState):

    user_input = state["user_input"]

    try:

        selected_tool = planner.plan(
            user_input
        ).strip()

    except Exception as e:

        print("\nPlanner Error:")
        print(e)

        selected_tool = "general"

    if selected_tool not in ALLOWED_TOOLS:

        print("\nInvalid planner output:")
        print(selected_tool)

        selected_tool = "general"

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

    response = ""

    try:

        # =====================================================
        # PDF SUMMARY
        # =====================================================

        if tool == "summarize":

            pdf_text = pdf_tool.get_latest_pdf_text()

            if not pdf_text.strip():

                response = "No PDF has been uploaded."

            else:

                response = llm_tool.summarize(
                    pdf_text
                )

        # =====================================================
        # PDF QUESTION ANSWERING
        # =====================================================

        elif tool == "question_answer":

            pdf_text = pdf_tool.get_latest_pdf_text()

            if not pdf_text.strip():

                response = "No PDF has been uploaded."

            else:

                response = llm_tool.answer_from_pdf(
                    pdf_text,
                    user_input,
                )

        # =====================================================
        # GENERAL CHAT
        # =====================================================

        elif tool == "general":

            response = llm_tool.answer_question(
                user_input
            )

        # =====================================================
        # WEB SEARCH
        # =====================================================

        elif tool == "web_search":

            response = web_tool.search(
                user_input
            )

        # =====================================================
        # TRANSLATION
        # =====================================================

        elif tool == "translate":

            response = llm_tool.translate(
                user_input
            )

        # =====================================================
        # SAVE PDF
        # =====================================================

        elif tool == "pdf_writer":

            previous = assistant_state.get_last_response()

            if previous.strip():

                path = pdf_writer.save(previous)

                response = (
                    "PDF saved successfully.\n\n"
                    f"{path}"
                )

            else:

                response = "No previous response available."

        # =====================================================
        # SAVE TXT
        # =====================================================

        elif tool == "txt_writer":

            previous = assistant_state.get_last_response()

            if previous.strip():

                path = txt_writer.save(previous)

                response = (
                    "TXT saved successfully.\n\n"
                    f"{path}"
                )

            else:

                response = "No previous response available."

        # =====================================================
        # WINDOWS CONTROL
        # =====================================================

        elif tool == "system_control":

            response = system_tool.execute(
                user_input
            )

        # =====================================================
        # FILE MANAGER
        # =====================================================

        elif tool == "file_manager":

            response = file_tool.execute(
                user_input
            )

        # =====================================================
        # OCR
        # =====================================================

        elif tool == "camera_reader":

            response = camera_tool.capture_text()

        # =====================================================
        # VISION AI
        # =====================================================

        elif tool == "vision_reader":

            response = vision_tool.describe_scene()

        # =====================================================
        # DOCUMENT CHAT
        # =====================================================

        elif tool == "document_chat":

            user_query = state["user_input"].lower()

            if "summar" in user_query:
                response = document_reader.summarize()

            elif "explain" in user_query:
                response = document_reader.explain()

            else:
                response = document_reader.answer(
                    state["user_input"]
                )

        # =====================================================
        # UNKNOWN TOOL
        # =====================================================

        else:

            response = (
                f"Unknown tool: {tool}"
            )

    except Exception as e:

        print("\n================ ERROR ================")
        traceback.print_exc()
        print("=======================================\n")

        response = str(e)

    print("\n" + "=" * 60)
    print("TOOL EXECUTED:", tool)
    print("=" * 60)
    print("Response:")
    print(response)
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
# LangGraph
# ============================================================

builder = StateGraph(
    AgentState
)

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