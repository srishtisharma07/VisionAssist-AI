from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage

from app.config.settings import settings
from app.services.assistant_state import assistant_state


class LLMTool:

    def __init__(self):

        self.llm = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            google_api_key=settings.GEMINI_API_KEY,
            temperature=0.3,
        )

    # =======================================================
    # Safe Gemini Call
    # =======================================================

    def _invoke(self, prompt: str) -> str:

        try:

            response = self.llm.invoke(
                [
                    HumanMessage(content=prompt)
                ]
            )

            return response.content.strip()

        except Exception as e:

            error = str(e).lower()

            # ------------------------------------
            # Quota Exceeded
            # ------------------------------------

            if (
                "resource_exhausted" in error
                or "429" in error
                or "quota" in error
            ):

                return (
                    "Gemini API quota has been exceeded.\n\n"
                    "Please use another API key or wait until "
                    "the quota resets."
                )

            # ------------------------------------
            # Invalid API Key
            # ------------------------------------

            if (
                "api_key_invalid" in error
                or "invalid api key" in error
                or "permission_denied" in error
            ):

                return (
                    "Invalid Gemini API Key.\n"
                    "Please update the API key."
                )

            # ------------------------------------
            # Network Error
            # ------------------------------------

            if (
                "connection" in error
                or "timeout" in error
                or "network" in error
            ):

                return (
                    "Unable to connect to Gemini.\n"
                    "Please check your internet connection."
                )

            # ------------------------------------
            # Unknown Error
            # ------------------------------------

            return f"Gemini Error:\n{str(e)}"

    # =======================================================
    # Summarize
    # =======================================================

    def summarize(self, text: str) -> str:

        prompt = f"""
You are an expert AI assistant.

Summarize the following text.

TEXT:

{text}
"""

        return self._invoke(prompt)

    # =======================================================
    # Translate
    # =======================================================

    def translate(self, text: str) -> str:

        prompt = f"""
Translate the following text into Hindi.

TEXT:

{text}
"""

        return self._invoke(prompt)

    # =======================================================
    # General Conversation
    # =======================================================

    def answer_question(self, question: str) -> str:

        history = assistant_state.build_history()

        prompt = f"""
You are VisionAssist AI.

Conversation History:

{history}

Current User Question:

{question}

Instructions:

- Use previous conversation whenever useful.
- If the user refers to previous messages using words like
  "it", "that", "this", "previous",
  understand the context.
- Otherwise answer normally.
- Keep responses concise and helpful.
"""

        return self._invoke(prompt)

    # =======================================================
    # PDF Question Answering
    # =======================================================

    def answer_from_pdf(
        self,
        pdf_text: str,
        question: str,
    ) -> str:

        history = assistant_state.build_history()

        prompt = f"""
You are VisionAssist AI.

Conversation History:

{history}

Answer ONLY using the uploaded PDF.

PDF:

{pdf_text}

Question:

{question}

If the answer does not exist inside the PDF,
reply exactly:

I could not find this information in the uploaded PDF.

Use previous conversation if needed.
"""

        return self._invoke(prompt)


llm_tool = LLMTool()