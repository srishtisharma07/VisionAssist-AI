from app.services.assistant_state import assistant_state


class PDFTool:

    def add_pdf(self, filename: str, text: str):

        assistant_state.add_pdf(
            filename=filename,
            text=text,
        )

    def get_latest_pdf_text(self) -> str:
        """
        Backward compatibility.
        Existing graph.py calls this function.
        Now it returns the combined text of all uploaded PDFs.
        """

        return assistant_state.get_all_pdf_text()

    def get_all_pdf_text(self) -> str:

        return assistant_state.get_all_pdf_text()

    def get_uploaded_pdfs(self):

        return assistant_state.get_all_pdfs()

    def remove_pdf(self, filename: str):

        assistant_state.remove_pdf(filename)

    def clear_pdfs(self):

        assistant_state.clear_pdfs()


pdf_tool = PDFTool()