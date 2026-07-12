from app.tools.llm_tool import ask_gemini


def general_question_answer(question: str):

    answer = ask_gemini(
        f"""
You are VisionAssist AI.

Answer the user's question clearly and accurately.

Question:

{question}
"""
    )

    return answer