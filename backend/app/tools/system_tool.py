import os
import subprocess
import webbrowser
import urllib.parse
from pathlib import Path
from app.tools.base_tool import BaseTool


class SystemTool(BaseTool):

    def open_folder(self, folder_name: str):
        home = Path.home()

        folders = {
            "downloads": home / "Downloads",
            "documents": home / "Documents",
            "desktop": home / "Desktop",
            "pictures": home / "Pictures",
            "videos": home / "Videos",
            "music": home / "Music",
        }

        folder = folders.get(folder_name.lower())

        if folder and folder.exists():
            os.startfile(folder)
            return f"Opening {folder_name.title()}."

        return f"{folder_name.title()} folder not found."

    def search_web(self, platform: str, query: str):
        query = urllib.parse.quote(query)

        if platform == "google":
            webbrowser.open(
                f"https://www.google.com/search?q={query}"
            )
            return f"Searching Google for {query}."

        if platform == "youtube":
            webbrowser.open(
                f"https://www.youtube.com/results?search_query={query}"
            )
            return f"Searching YouTube for {query}."

        if platform == "github":
            webbrowser.open(
                f"https://github.com/search?q={query}"
            )
            return f"Searching GitHub for {query}."

        return "Unknown search platform."

    def execute(self, command: str):
        command = command.lower()

        # -------------------------
        # Search Commands
        # -------------------------
        if command.startswith("search google for"):
            query = command.replace("search google for", "").strip()
            return self.search_web("google", query)

        if command.startswith("search youtube for"):
            query = command.replace("search youtube for", "").strip()
            return self.search_web("youtube", query)

        if command.startswith("search github for"):
            query = command.replace("search github for", "").strip()
            return self.search_web("github", query)

        # -------------------------
        # Common Windows Folders
        # -------------------------
        if "downloads" in command:
            return self.open_folder("downloads")
        if "documents" in command:
            return self.open_folder("documents")
        if "desktop" in command:
            return self.open_folder("desktop")
        if "pictures" in command:
            return self.open_folder("pictures")
        if "videos" in command:
            return self.open_folder("videos")
        if "music" in command:
            return self.open_folder("music")

        # -------------------------
        # Browsers
        # -------------------------

        if "chrome" in command:
            os.system("start chrome")
            return "Opening Google Chrome."

        if "google" in command:
            webbrowser.open("https://google.com")
            return "Opening Google."

        if "youtube" in command:
            webbrowser.open("https://youtube.com")
            return "Opening YouTube."

        if "gmail" in command:
            webbrowser.open("https://mail.google.com")
            return "Opening Gmail."

        if "github" in command:
            webbrowser.open("https://github.com")
            return "Opening GitHub."

        # -------------------------
        # Editors
        # -------------------------

        if "vs code" in command or "code" in command:
            os.system("code")
            return "Opening VS Code."

        if "notepad" in command:
            os.system("notepad")
            return "Opening Notepad."

        if "paint" in command:
            os.system("mspaint")
            return "Opening Paint."

        # -------------------------
        # Windows Apps
        # -------------------------

        if "calculator" in command:
            os.system("calc")
            return "Opening Calculator."

        if "command prompt" in command or "cmd" in command:
            subprocess.Popen("cmd")
            return "Opening Command Prompt."

        if "file explorer" in command or "explorer" in command:
            subprocess.Popen("explorer")
            return "Opening File Explorer."

        if "settings" in command:
            os.system("start ms-settings:")
            return "Opening Windows Settings."

        return "Unsupported system command."


system_tool = SystemTool()