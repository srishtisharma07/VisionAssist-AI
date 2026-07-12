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

        # Save extracted text as TXT
        txt_path = Path(file_path).with_suffix(".txt")

        with open(txt_path, "w", encoding="utf-8") as txt_file:
            txt_file.write(text)

        print("=" * 60)
        print(f"Total Characters Extracted: {len(text)}")
        print(f"Text File Saved: {txt_path}")
        print("=" * 60 + "\n")

        return text

    def get_text(self):

        return self.current_text

    def get_latest_text_file(self):

        txt_files = sorted(
            self.upload_dir.glob("*.txt"),
            key=lambda x: x.stat().st_mtime,
            reverse=True,
        )

        if not txt_files:
            return ""

        return txt_files[0].read_text(
            encoding="utf-8",
            errors="ignore",
        )


pdf_service = PDFService()