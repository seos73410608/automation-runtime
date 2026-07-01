import glob

from fastapi import (
    APIRouter,
    Request
)
from fastapi.responses import FileResponse
from fastapi.templating import Jinja2Templates

from app.db.database import SessionLocal
from app.db.repository import AutomationRepository

router = APIRouter()

templates = Jinja2Templates(
    directory="app/templates"
)


@router.get("/history")
def history(request: Request):

    db = SessionLocal()

    try:

        repo = AutomationRepository(db)

        jobs = repo.get_jobs()

        return templates.TemplateResponse(
            request=request,
            name="history.html",
            context={
                "jobs": jobs
            }
        )

    finally:

        db.close()


@router.get("/job/{job_id}")
def job_detail(
    request: Request,
    job_id: str
):

    db = SessionLocal()

    try:

        repo = AutomationRepository(db)

        job = repo.find_job(job_id)

        histories = repo.find_history(job_id)

        return templates.TemplateResponse(
            request=request,
            name="job_detail.html",
            context={
                "job": job,
                "histories": histories
            }
        )

    finally:

        db.close()


@router.get("/download/{job_id}")
def download(job_id: str):

    matches = glob.glob(
        f"output/*/{job_id}/result.zip"
    )

    if not matches:

        return {
            "success": False,
            "message": "ZIP 파일이 존재하지 않습니다."
        }

    zip_path = matches[0]

    return FileResponse(
        path=zip_path,
        filename="result.zip",
        media_type="application/zip"
    )