from pathlib import Path

from fastapi import FastAPI
from fastapi import Request
from fastapi import UploadFile
from fastapi import Form

from fastapi.responses import FileResponse
from fastapi.templating import Jinja2Templates

from app.jobs.repair_pending_job import RepairPendingJob

app = FastAPI(
    title="Automation Runtime",
    version="0.4.0"
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
    job: str=Form(...)
):

    input_dir = Path("input")

    input_dir.mkdir(
        exist_ok=True
    )

    # 기존 파일 제거
    for old_file in input_dir.glob("*"):

        if old_file.is_file():

            old_file.unlink()

    save_path = input_dir / file.filename

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
            .execute()
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
