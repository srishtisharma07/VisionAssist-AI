class Router:

    def route(self, command: str) -> str:

        command = command.lower()

        if any(word in command for word in [
            "summarize",
            "summary",
            "summarise"
        ]):
            return "summarize"

        if any(word in command for word in [
            "explain",
            "describe",
            "teach"
        ]):
            return "explain"

        if any(word in command for word in [
            "translate",
            "hindi",
            "english"
        ]):
            return "translate"

        if any(word in command for word in [
            "save pdf",
            "export pdf"
        ]):
            return "pdf_writer"

        if any(word in command for word in [
            "save txt",
            "text file"
        ]):
            return "txt_writer"

        return "question_answer"


router = Router()