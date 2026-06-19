from pathlib import Path
from datetime import datetime
import uuid

from fastapi import FastAPI
from fastapi import Request
from fastapi import UploadFile
from fastapi import Form

from fastapi.responses import FileResponse
from fastapi.templating import Jinja2Templates

from app.jobs.repair_pending_job import RepairPendingJob

from app.db.database import SessionLocal
from app.db.repository import AutomationRepository

app = FastAPI(
    title="Automation Runtime",
    version="0.5.0"
)

templates = Jinja2Templates(
    directory="app/templates"
)


@app.get("/")
def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={}
    )


@app.post("/run")
async def run_job(
    request: Request,
    file: UploadFile,
    job: str = Form(...)
):

    job_id = str(
        uuid.uuid4()
    )

    upload_dir = (
        Path("uploads")
        / datetime.now().strftime("%Y%m%d")
        / job_id
    )

    upload_dir.mkdir(
        parents=True,
        exist_ok=True
    )

    save_path = (
        upload_dir
        / file.filename
    )

    with open(
        save_path,
        "wb"
    ) as f:

        f.write(
            await file.read()
        )

    if job == "repair_pending":

        result = (
            RepairPendingJob()
            .execute(
                job_id=job_id,
                file_name=file.filename,
                file_path=str(save_path)
            )
        )

        return templates.TemplateResponse(
            request=request,
            name="result.html",
            context={
                "result": result
            }
        )

    return templates.TemplateResponse(
        request=request,
        name="result.html",
        context={
            "result": {
                "job_name": job,
                "success": False,
                "message": "지원하지 않는 Job"
            }
        }
    )


@app.get("/history")
def history(
    request: Request
):

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


@app.get("/job/{job_id}")
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


@app.get("/download")
def download():

    zip_path = Path(
        "output/result.zip"
    )

    if not zip_path.exists():

        return {
            "success": False,
            "message": "ZIP 파일이 존재하지 않습니다."
        }

    return FileResponse(
        path=zip_path,
        filename="result.zip",
        media_type="application/zip"
    )