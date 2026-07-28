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
        self.pictures = Path.home() / "Pictures"
        self.videos = Path.home() / "Videos"
        self.music = Path.home() / "Music"

    # -----------------------------------------------------

    def contains_any(self, text, words):
        return any(word in text for word in words)

    # -----------------------------------------------------

    def _extract_name(self, command: str):
        text = command.strip()
        lower = text.lower()

        prefixes = [
            "create folder named",
            "create folder",
            "folder named",
            "new folder",
            "make folder",
            "create file named",
            "create file",
            "file named",
            "new file",
            "make file",
            "delete folder named",
            "delete folder",
            "delete file named",
            "delete file",
            "remove folder",
            "remove file",
            "rename folder",
            "rename file",
        ]

        for prefix in prefixes:
            if lower.startswith(prefix):
                return text[len(prefix) :].strip()

        return text

    # -----------------------------------------------------

    def get_special_folder(self, text):
        text = text.lower()

        if "desktop" in text:
            return self.desktop

        if "downloads" in text:
            return self.downloads

        if "documents" in text:
            return self.documents

        if "pictures" in text:
            return self.pictures

        if "videos" in text:
            return self.videos

        if "music" in text:
            return self.music

        return None

    # -----------------------------------------------------

    def execute(self, command):
        lower = command.lower().strip()

        try:
            # =====================================================
            # OPEN FOLDERS
            # =====================================================

            if ("open" in lower or "show" in lower) and self.contains_any(
                lower,
                [
                    "desktop",
                    "downloads",
                    "documents",
                    "pictures",
                    "videos",
                    "music",
                ],
            ):
                folder = self.get_special_folder(lower)

                if folder is None:
                    return "Folder not found."

                subprocess.Popen(["explorer", str(folder)])

                return f"Opening {folder.name}."

            # =====================================================
            # CREATE FOLDER
            # =====================================================

            if (
                "create folder" in lower
                or "folder named" in lower
                or "new folder" in lower
                or "make folder" in lower
            ):
                folder_name = self._extract_name(command)

                if not folder_name:
                    return "Please provide a folder name."

                folder = self.desktop / folder_name
                folder.mkdir(
                    parents=True,
                    exist_ok=True,
                )

                return f"Folder '{folder_name}' created successfully."

            # =====================================================
            # CREATE FILE
            # =====================================================

            if (
                "create file" in lower
                or "file named" in lower
                or "new file" in lower
                or "make file" in lower
            ):
                file_name = self._extract_name(command)

                if not file_name:
                    return "Please provide a file name."

                file_path = self.desktop / file_name
                file_path.touch(
                    exist_ok=True,
                )

                return f"File '{file_name}' created successfully."

            # =====================================================
            # DELETE FOLDER
            # =====================================================

            if (
                "delete folder" in lower
                or "remove folder" in lower
            ):
                folder_name = self._extract_name(command)
                folder = self.desktop / folder_name

                if not folder.exists():
                    return "Folder not found."

                shutil.rmtree(folder)

                return f"Folder '{folder_name}' deleted successfully."

            # =====================================================
            # DELETE FILE
            # =====================================================

            if (
                "delete file" in lower
                or "remove file" in lower
            ):
                file_name = self._extract_name(command)
                file_path = self.desktop / file_name

                if not file_path.exists():
                    return "File not found."

                file_path.unlink()

                return f"Deleted '{file_name}'."

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

                return f"Folder renamed to '{new_name.strip()}'."

            # =====================================================
            # COPY FILE
            # =====================================================

            if "copy file" in lower:
                text = lower.replace(
                    "copy file",
                    "",
                ).strip()

                if " to " not in text:
                    return "Use: Copy file FILE to DESTINATION."

                filename, destination = text.split(
                    " to ",
                    1,
                )

                source = self.desktop / filename.strip()

                if not source.exists():
                    return "File not found."

                target = self.get_special_folder(destination)

                if target is None:
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
                    return "Use: Move file FILE to DESTINATION."

                filename, destination = text.split(
                    " to ",
                    1,
                )

                source = self.desktop / filename.strip()

                if not source.exists():
                    return "File not found."

                target = self.get_special_folder(destination)

                if target is None:
                    target = self.desktop

                shutil.move(
                    str(source),
                    str(target),
                )

                return "File moved successfully."

            # =====================================================
            # LIST FILES
            # =====================================================

            if (
                "list" in lower
                or "show files" in lower
                or "what files" in lower
            ):
                folder = self.get_special_folder(lower)

                if folder is None:
                    folder = self.desktop

                if not folder.exists():
                    return "Folder does not exist."

                files = os.listdir(folder)

                if not files:
                    return f"{folder.name} is empty."

                return f"Files in {folder.name}:\n\n" + "\n".join(files)

            # =====================================================
            # UNKNOWN COMMAND
            # =====================================================

            return "Unsupported file command."

        except Exception as e:
            return f"File Tool Error: {str(e)}"


file_tool = FileTool()