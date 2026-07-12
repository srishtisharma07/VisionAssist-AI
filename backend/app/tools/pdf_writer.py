from pathlib import Path
from datetime import datetime

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer


class PDFWriter:

    def __init__(self):

        self.output_dir = Path("app/outputs")
        self.output_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

    def save(self, text: str) -> str:

        filename = (
            f"visionassist_"
            f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
        )

        file_path = self.output_dir / filename

        document = SimpleDocTemplate(str(file_path))

        styles = getSampleStyleSheet()

        story = []

        title = Paragraph(
            "<b><font size=18>VisionAssist AI</font></b>",
            styles["Title"],
        )

        subtitle = Paragraph(
            "<b>Generated Response</b>",
            styles["Heading2"],
        )

        content = Paragraph(
            text.replace("\n", "<br/>"),
            styles["BodyText"],
        )

        generated_time = Paragraph(
            f"<b>Generated on:</b> {datetime.now().strftime('%d %B %Y %H:%M:%S')}",
            styles["Normal"],
        )

        story.append(title)
        story.append(Spacer(1, 20))

        story.append(subtitle)
        story.append(Spacer(1, 20))

        story.append(content)
        story.append(Spacer(1, 30))

        story.append(generated_time)

        document.build(story)

        return str(file_path)


pdf_writer = PDFWriter()