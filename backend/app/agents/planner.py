from app.prompts.planner_prompt import PLANNER_PROMPT
from app.tools.llm_tool import llm_tool


class Planner:

    def __init__(self):
        pass

    def contains_any(self, text, keywords):
        return any(keyword in text for keyword in keywords)

    def plan(self, command: str):

        text = command.lower().strip()

        # ==================================================
        # Vision AI
        # ==================================================

        vision_keywords = [
            "describe",
            "what do you see",
            "what is in front",
            "identify",
            "objects",
            "room",
            "surroundings",
            "scene",
            "look around",
            "can you see",
            "what is on my desk",
            "what's on my desk",
            "describe the room",
            "describe surroundings",
        ]

        if self.contains_any(text, vision_keywords):
            return "vision_reader"

        # ==================================================
        # OCR
        # ==================================================

        ocr_keywords = [
            "read this page",
            "read page",
            "read this document",
            "read document",
            "scan page",
            "scan document",
            "scan this",
            "read text",
            "extract text",
        ]

        if self.contains_any(text, ocr_keywords):
            return "camera_reader"

        # ==================================================
        # File Manager
        # ==================================================

        file_keywords = [
            # Create
            "create folder",
            "create file",
            "new folder",
            "new file",
            "make folder",
            "make file",
            "folder named",
            "file named",

            # Delete
            "delete folder",
            "delete file",
            "remove folder",
            "remove file",

            # Rename
            "rename folder",
            "rename file",

            # Move / Copy
            "move file",
            "copy file",

            # Open
            "open downloads",
            "open desktop",
            "open documents",
            "open pictures",

            # List
            "list desktop",
            "list downloads",
            "list documents",
            "list pictures",
        ]

        if any(keyword in text for keyword in file_keywords):
            return "file_manager"

        # ==================================================
        # Windows Control
        # ==================================================

        system_keywords = [

            "open chrome",
            "open edge",
            "open firefox",

            "open calculator",

            "open paint",

            "open notepad",

            "open vscode",
            "open vs code",
            "open visual studio code",

            "open youtube",
            "open gmail",
            "open google",

            "shutdown computer",
            "restart computer",
            "lock computer",

        ]

        if self.contains_any(text, system_keywords):
            return "system_control"

        # ==================================================
        # Translation
        # ==================================================

        if (
            "translate" in text
            or "convert to hindi" in text
            or "translate this" in text
        ):
            return "translate"

        # ==================================================
        # PDF Summary
        # ==================================================

        if (
            "summarize" in text
            or "summary" in text
            or "important points" in text
            or "notes from pdf" in text
        ):
            return "summarize"

        # ==================================================
        # Save Response
        # ==================================================

        if (
            "save as pdf" in text
            or "export pdf" in text
        ):
            return "pdf_writer"

        if (
            "save as txt" in text
            or "save as text" in text
            or "export text" in text
        ):
            return "txt_writer"

        # ==================================================
        # Web Search
        # ==================================================

        web_keywords = [

            "latest",
            "today",
            "news",
            "weather",
            "live score",
            "current",
            "stock price",
            "latest ai",
            "breaking news",

        ]

        if self.contains_any(text, web_keywords):
            return "web_search"

        # ==================================================
        # PDF QA
        # ==================================================

        pdf_keywords = [

            "page",
            "pdf",
            "author",
            "chapter",

        ]

        if self.contains_any(text, pdf_keywords):
            return "question_answer"

        # ==================================================
        # Gemini Fallback
        # ==================================================

        prompt = (
            PLANNER_PROMPT
            + "\n\nUser Command:\n"
            + command
            + "\n\nReturn ONLY one tool name."
        )

        try:

            result = llm_tool._invoke(prompt).strip()

            allowed = {
                "general",
                "question_answer",
                "summarize",
                "translate",
                "pdf_writer",
                "txt_writer",
                "web_search",
                "system_control",
                "camera_reader",
                "file_manager",
                "vision_reader",
            }

            if result in allowed:
                return result

            return "general"

        except Exception:

            return "general"


planner = Planner()