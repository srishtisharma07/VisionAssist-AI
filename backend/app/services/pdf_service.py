import shutil
from pathlib import Path

import fitz


class PDFService:

    def __init__(self):
        self.upload_dir = Path("app/uploads")
        self.upload_dir.mkdir(parents=True, exist_ok=True)

        self.current_text = ""

    def save_pdf(self, file):

        file_path = self.upload_dir / file.filename

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        return str(file_path)

    def extract_text(self, file_path: str):

        document = fitz.open(file_path)

        text = ""

        print("\n" + "=" * 60)
        print("PDF EXTRACTION STARTED")
        print("=" * 60)

        print(f"File: {file_path}")
        print(f"Total Pages: {len(document)}")

        for page_number, page in enumerate(document):

            page_text = page.get_text()

            print(
                f"Page {page_number + 1}: {len(page_text)} characters extracted"
            )

            text += page_text

        document.close()

        self.current_text = text

        print("=" * 60)
        print(f"Total Characters Extracted: {len(text)}")
        print("=" * 60 + "\n")

        return text

    def get_text(self):

        return self.current_text


pdf_service = PDFService()