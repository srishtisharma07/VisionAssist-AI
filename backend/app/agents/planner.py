from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage

from app.config import settings
from app.prompts import PLANNER_PROMPT


class Planner:

    def __init__(self):

        self.llm = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            google_api_key=settings.GEMINI_API_KEY,
            temperature=0,
        )

    def plan(self, user_request: str) -> str:

        prompt = f"""
{PLANNER_PROMPT}

User Request:

{user_request}

Tool:
"""

        response = self.llm.invoke(
            [
                HumanMessage(content=prompt)
            ]
        )

        tool = response.content.strip().lower()

        allowed_tools = {
            "general",
            "question_answer",
            "summarize",
            "translate",
            "pdf_writer",
            "txt_writer",
            "web_search",
        }

        if tool not in allowed_tools:

            tool = "general"

        return tool


planner = Planner()