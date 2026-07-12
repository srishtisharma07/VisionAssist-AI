from fastapi import APIRouter, File, HTTPException, UploadFile

from app.services.pdf_service import pdf_service
from app.services.assistant_state import assistant_state
from app.tools.pdf_tool import pdf_tool

router = APIRouter(
    prefix="/pdf",
    tags=["PDF"],
)


@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):

    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed.",
        )

    # Save PDF
    path = pdf_service.save_pdf(file)

    # Extract text
    extracted_text = pdf_service.extract_text(path)

    # Store in Assistant State
    pdf_tool.add_pdf(
        filename=file.filename,
        text=extracted_text,
    )

    return {
        "message": "PDF uploaded successfully.",
        "file_name": file.filename,
        "characters_extracted": len(extracted_text),
        "total_uploaded_pdfs": len(pdf_tool.get_uploaded_pdfs()),
        "preview": extracted_text[:500],
    }


@router.get("/text")
def get_pdf_text():

    return {
        "text": pdf_tool.get_all_pdf_text()
    }


@router.get("/info")
def get_pdf_info():

    pdfs = pdf_tool.get_uploaded_pdfs()

    return {
        "total_pdfs": len(pdfs),
        "uploaded_pdfs": [
            pdf["filename"]
            for pdf in pdfs
        ],
        "characters": len(
            pdf_tool.get_all_pdf_text()
        ),
    }


@router.delete("/clear")
def clear_all_pdfs():

    pdf_tool.clear_pdfs()

    return {
        "message": "All PDFs removed successfully."
    }


@router.delete("/{filename}")
def delete_pdf(filename: str):

    pdf_tool.remove_pdf(filename)

    return {
        "message": f"{filename} removed successfully."
    }