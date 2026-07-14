import os
import subprocess
import webbrowser

from app.tools.base_tool import BaseTool


class SystemTool(BaseTool):

    def execute(self, command: str):

        command = command.lower()

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