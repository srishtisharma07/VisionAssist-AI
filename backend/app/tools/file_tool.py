import os
import shutil
import subprocess
from pathlib import Path

from app.tools.base_tool import BaseTool


class FileTool(BaseTool):

    def __init__(self):

        self.desktop = Path.home() / "Desktop"
        self.documents = Path.home() / "Documents"
        self.downloads = Path.home() / "Downloads"

    # --------------------------------------------------------

    def _extract_name(self, command: str, keyword: str):

        text = command.lower()

        if "named" in text:
            return command.split("named", 1)[1].strip()

        return command.split(keyword, 1)[1].strip()

    # --------------------------------------------------------

    def execute(self, command: str):

        lower = command.lower()

        try:

            # =====================================================
            # OPEN
            # =====================================================

            if "open desktop" in lower:

                subprocess.Popen(["explorer", str(self.desktop)])

                return "Opening Desktop."

            if "open documents" in lower:

                subprocess.Popen(["explorer", str(self.documents)])

                return "Opening Documents."

            if "open downloads" in lower:

                subprocess.Popen(["explorer", str(self.downloads)])

                return "Opening Downloads."

            # =====================================================
            # CREATE FOLDER
            # =====================================================

            if "create folder" in lower:

                folder_name = self._extract_name(
                    command,
                    "folder",
                )

                folder = self.desktop / folder_name

                folder.mkdir(
                    parents=True,
                    exist_ok=True,
                )

                return f"Folder '{folder_name}' created successfully."

            # =====================================================
            # CREATE FILE
            # =====================================================

            if "create file" in lower:

                file_name = self._extract_name(
                    command,
                    "file",
                )

                file_path = self.desktop / file_name

                file_path.touch(
                    exist_ok=True,
                )

                return f"File '{file_name}' created successfully."

            # =====================================================
            # DELETE FILE
            # =====================================================

            if "delete file" in lower:

                file_name = self._extract_name(
                    command,
                    "file",
                )

                file_path = self.desktop / file_name

                if not file_path.exists():

                    return "File not found."

                file_path.unlink()

                return f"Deleted file '{file_name}'."

            # =====================================================
            # DELETE FOLDER
            # =====================================================

            if "delete folder" in lower:

                folder_name = self._extract_name(
                    command,
                    "folder",
                )

                folder = self.desktop / folder_name

                if not folder.exists():

                    return "Folder not found."

                shutil.rmtree(folder)

                return f"Deleted folder '{folder_name}'."

            # =====================================================
            # RENAME FOLDER
            # =====================================================

            if "rename folder" in lower:

                text = lower.replace(
                    "rename folder",
                    "",
                ).strip()

                if " to " not in text:

                    return "Use: Rename folder OLD to NEW."

                old_name, new_name = text.split(
                    " to ",
                    1,
                )

                old_folder = self.desktop / old_name.strip()

                new_folder = self.desktop / new_name.strip()

                if not old_folder.exists():

                    return "Folder not found."

                old_folder.rename(new_folder)

                return "Folder renamed successfully."

            # =====================================================
            # COPY FILE
            # =====================================================

            if "copy file" in lower:

                text = lower.replace(
                    "copy file",
                    "",
                ).strip()

                if " to " not in text:

                    return "Use: Copy file A to Documents."

                filename, destination = text.split(
                    " to ",
                    1,
                )

                source = self.desktop / filename.strip()

                if not source.exists():

                    return "File not found."

                destination = destination.strip()

                if destination == "documents":

                    target = self.documents

                elif destination == "downloads":

                    target = self.downloads

                else:

                    target = self.desktop

                shutil.copy2(
                    source,
                    target,
                )

                return "File copied successfully."

            # =====================================================
            # MOVE FILE
            # =====================================================

            if "move file" in lower:

                text = lower.replace(
                    "move file",
                    "",
                ).strip()

                if " to " not in text:

                    return "Use: Move file A to Documents."

                filename, destination = text.split(
                    " to ",
                    1,
                )

                source = self.desktop / filename.strip()

                if not source.exists():

                    return "File not found."

                destination = destination.strip()

                if destination == "documents":

                    target = self.documents

                elif destination == "downloads":

                    target = self.downloads

                else:

                    target = self.desktop

                shutil.move(
                    str(source),
                    str(target),
                )

                return "File moved successfully."

            # =====================================================
            # LIST FILES
            # =====================================================

            if "list desktop" in lower:

                files = os.listdir(
                    self.desktop
                )

                if not files:

                    return "Desktop is empty."

                return "\n".join(files)

            return "Unsupported file command."

        except Exception as e:

            return f"Error: {str(e)}"


file_tool = FileTool()