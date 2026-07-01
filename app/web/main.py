from fastapi import FastAPI
from fastapi.templating import Jinja2Templates

from app.scheduler.scheduler_manager import SchedulerManager

from app.web.routes.dashboard import router as dashboard_router
from app.web.routes.jobs import router as jobs_router
from app.web.routes.history import router as history_router


app = FastAPI(
    title="Automation Runtime",
    version="0.7.1"
)

templates = Jinja2Templates(
    directory="app/templates"
)

scheduler_manager = SchedulerManager()


@app.on_event("startup")
def startup():

    scheduler_manager.start()


@app.on_event("shutdown")
def shutdown():

    scheduler_manager.shutdown()


#
# Router 등록
#
app.include_router(
    dashboard_router
)

app.include_router(
    jobs_router
)

app.include_router(
    history_router
)