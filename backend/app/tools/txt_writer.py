from pathlib import Path
from datetime import datetime


class TXTWriter:

    def __init__(self):

        self.output_dir = Path("app/outputs")
        self.output_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

    def save(self, text: str) -> str:

        filename = (
            f"visionassist_"
            f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        )

        file_path = self.output_dir / filename

        with open(
            file_path,
            "w",
            encoding="utf-8",
        ) as file:

            file.write(text)

        return str(file_path)


txt_writer = TXTWriter()