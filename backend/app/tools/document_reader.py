from app.tools.camera_tool import camera_tool
from app.tools.llm_tool import llm_tool


class DocumentReader:

    def read(self):

        text = camera_tool.capture_text()

        if not text:

            return "No text could be detected."

        return text

    def summarize(self):

        text = camera_tool.capture_text()

        if not text:

            return "No text could be detected."

        return llm_tool.summarize(text)

    def explain(self):

        text = camera_tool.capture_text()

        if not text:

            return "No text could be detected."

        prompt = f"""
Explain the following document.

{text}
"""

        return llm_tool.answer_question(prompt)


document_reader = DocumentReader()