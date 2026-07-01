from pathlib import Path
from datetime import datetime

from fastapi import (
    APIRouter,
    Request,
    UploadFile,
    Form
)
from fastapi.templating import Jinja2Templates
from sqlalchemy import text

from app.db.database import SessionLocal
from app.runtime.runtime_service import RuntimeService

router = APIRouter()

templates = Jinja2Templates(
    directory="app/templates"
)

runtime_service = RuntimeService()


@router.post("/run")
async def run_job(
    request: Request,
    file: UploadFile,
    job: str = Form(...)
):

    #
    # 등록된 Job ID 조회
    #
    db = SessionLocal()

    job_id = db.execute(
        text("""
            SELECT job_id
            FROM tb_automation_job
            WHERE job_name = :job_name
        """),
        {
            "job_name": job
        }
    ).scalar()

    db.close()

    if job_id is None:

        return templates.TemplateResponse(
            request=request,
            name="result.html",
            context={
                "result": {
                    "success": False,
                    "message": f"등록되지 않은 Job : {job}"
                }
            }
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