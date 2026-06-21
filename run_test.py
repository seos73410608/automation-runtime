from app.runtime.runtime_service import RuntimeService

runtime = RuntimeService()

result = runtime.execute(
    job_name="repair_pending",
    job_id="test-002",
    file_name="A_S접수현황.xls",
    file_path="C:/SeoS/Claude/sample/A_S접수현황.xls"
)

print(result)
