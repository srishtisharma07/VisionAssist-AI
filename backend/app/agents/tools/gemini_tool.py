from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage

from app.config import settings
from app.services.pdf_service import pdf_service


class GeminiTool:

    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            google_api_key=settings.GEMINI_API_KEY,
            temperature=0.3,
        )

    def summarize(self, text: str):

        pdf_text = pdf_service.get_text()

        if pdf_text:

            prompt = f"""
Summarize the following PDF in simple bullet points.

PDF Content:

{pdf_text}
"""

        else:

            prompt = f"""
Summarize the following text.

{text}
"""

        response = self.llm.invoke(
            [HumanMessage(content=prompt)]
        )

        return response.content

    def explain(self, text: str):

        pdf_text = pdf_service.get_text()

        if pdf_text:

            prompt = f"""
Using ONLY the PDF content below, explain the user's question.

PDF Content:

{pdf_text}

User Question:

{text}

If the answer is not present in the PDF,
reply with:

"I couldn't find this information in the uploaded PDF."
"""

        else:

            prompt = f"""
Explain the following topic.

{text}
"""

        response = self.llm.invoke(
            [HumanMessage(content=prompt)]
        )

        return response.content

    def translate(self, text: str):

        prompt = f"""
Translate the following into Hindi.

{text}
"""

        response = self.llm.invoke(
            [HumanMessage(content=prompt)]
        )

        return response.content

    def answer_question(self, question: str):

        pdf_text = pdf_service.get_text()

        if pdf_text:

            prompt = f"""
Answer ONLY using the PDF below.

PDF:

{pdf_text}

Question:

{question}

If the answer is unavailable in the PDF,
say:

"I couldn't find this information in the uploaded PDF."
"""

        else:

            prompt = question

        response = self.llm.invoke(
            [HumanMessage(content=prompt)]
        )

        return response.content


gemini_tool = GeminiTool()