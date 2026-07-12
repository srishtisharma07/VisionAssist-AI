def build_pdf_prompt(pdf_text: str, question: str) -> str:

    return f"""
You are an AI assistant.

Answer the user's question ONLY using the uploaded PDF.

If the answer is not available in the PDF, reply exactly:

I couldn't find this information in the uploaded PDF.

-------------------------
PDF CONTENT
-------------------------

{pdf_text}

-------------------------
QUESTION
-------------------------

{question}

-------------------------
ANSWER
-------------------------
"""