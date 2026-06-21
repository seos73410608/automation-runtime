from pathlib import Path
from datetime import datetime
import uuid
import glob

from fastapi import FastAPI, Request, UploadFile, Form
from fastapi.responses import FileResponse
from fastapi.templating import Jinja2Templates

from app.runtime.runtime_service import RuntimeService

from app.db.database import SessionLocal
from app.db.repository import AutomationRepository

from app.scheduler.scheduler_manager import SchedulerManager

app = FastAPI(
    title="Automation Runtime",
    version="0.7.1"
)

templates = Jinja2Templates(
    directory="app/templates"
)

scheduler_manager = SchedulerManager()

runtime_service = RuntimeService()


@app.on_event("startup")
def startup():

    scheduler_manager.start()


@app.on_event("shutdown")
def shutdown():

    scheduler_manager.shutdown()


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
    job: str=Form(...)
):

    job_id = str(uuid.uuid4())

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

    try:

        result = runtime_service.execute(
            job_name=job,
            job_id=job_id,
            file_name=file.filename,
            file_path=str(save_path)
        )

    except Exception as e:

        result = {
            "job_name": job,
            "success": False,
            "message": str(e)
        }

    return templates.TemplateResponse(
        request=request,
        name="result.html",
        context={
            "result": result
        }
    )


@app.get("/history")
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


@app.get("/download/{job_id}")
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
