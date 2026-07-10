from fastapi import APIRouter, File, HTTPException, UploadFile

from app.services.pdf_service import pdf_service

router = APIRouter(
    prefix="/pdf",
    tags=["PDF"],
)


@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):

    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed."
        )

    path = pdf_service.save_pdf(file)

    extracted_text = pdf_service.extract_text(path)

    return {
        "message": "PDF uploaded successfully.",
        "file_name": file.filename,
        "characters_extracted": len(extracted_text),
        "preview": extracted_text[:500],
    }


@router.get("/text")
def get_pdf_text():

    return {
        "text": pdf_service.get_text()
    }