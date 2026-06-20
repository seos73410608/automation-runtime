from app.jobs.repair_pending_job import RepairPendingJob

job = RepairPendingJob()

job.execute(
    job_id="test-001",
    file_name="A_S접수현황.xls",
    file_path="C:/SeoS/Claude/sample/A_S접수현황.xls"
)
