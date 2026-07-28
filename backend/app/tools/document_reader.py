from app.services.assistant_state import assistant_state
from app.tools.camera_tool import camera_tool
from app.tools.llm_tool import llm_tool


class DocumentReader:

    def read(self):

        text = camera_tool.capture_text()

        if not text:
            return "No text could be detected."

        return text

    def explain(self):

        document = assistant_state.get_current_document()

        if not document.strip():
            return "No document has been scanned yet."

        prompt = f"""
Explain the following document in simple language.

{document}
"""

        return llm_tool.answer_question(prompt)

    def summarize(self):

        document = assistant_state.get_current_document()

        if not document.strip():
            return "No document has been scanned yet."

        return llm_tool.summarize(document)

    def answer(self, question):

        document = assistant_state.get_current_document()

        if not document.strip():
            return "No document has been scanned yet."

        prompt = f"""
You are VisionAssist AI.

Answer ONLY using this document.

Document:
-------------------
{document}
-------------------

Question:
{question}

If the answer is not present,
say that it isn't available in the document.
"""

        return llm_tool.answer_question(prompt)


document_reader = DocumentReader()