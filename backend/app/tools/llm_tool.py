from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage

from app.config.settings import settings
from app.prompts.pdf_prompt import build_pdf_prompt
from app.services.assistant_state import assistant_state


class LLMTool:

    def __init__(self):

        self.llm = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            google_api_key=settings.GEMINI_API_KEY,
            temperature=0.3,
        )

    def _invoke(self, prompt: str) -> str:

        response = self.llm.invoke(
            [
                HumanMessage(content=prompt)
            ]
        )

        return response.content.strip()

    def summarize(self, text: str) -> str:

        prompt = f"""
You are an expert AI assistant.

Summarize the following text.

TEXT:

{text}
"""

        return self._invoke(prompt)

    def translate(self, text: str) -> str:

        prompt = f"""
Translate the following text into Hindi.

TEXT:

{text}
"""

        return self._invoke(prompt)

    def answer_question(self, question: str) -> str:

        history = assistant_state.build_history()

        prompt = f"""
You are VisionAssist AI.

Below is the previous conversation.

{history}

Current User Question:

{question}

Instructions:

- Use previous conversation whenever useful.
- If the current question refers to previous answers using words like
  "it", "that", "this", "previous", "explain more",
  understand the context.
- If there is no previous context, answer normally.
- Give clear and concise answers.
"""

        return self._invoke(prompt)

    def answer_from_pdf(self, pdf_text: str, question: str) -> str:

        history = assistant_state.build_history()

        prompt = f"""
You are VisionAssist AI.

Conversation History:

{history}

Answer ONLY using the PDF below.

PDF:

{pdf_text}

Question:

{question}

If the answer is not present in the PDF,
say:

"I could not find this information in the uploaded PDF."

Use previous conversation if needed.
"""

        return self._invoke(prompt)


llm_tool = LLMTool()