from app.jobs.job_registry import JOB_REGISTRY
from app.utils.logger import logger


def main():

    job_name = "repair_pending"

    job = JOB_REGISTRY[job_name]()

    result = job.execute()

    logger.info("==================================")
    logger.info(f"JOB          : {result.job_name}")
    logger.info(f"TOTAL ROWS   : {result.total_rows}")
    logger.info(f"FILTERED     : {result.filtered_rows}")
    logger.info(f"VENDORS      : {result.vendor_count}")
    logger.info(f"OUTPUT FILES : {result.output_file_count}")
    logger.info(f"ZIP FILE     : {result.zip_file_path}")
    logger.info(f"SUCCESS      : {result.success}")
    logger.info(f"MESSAGE      : {result.message}")
    logger.info("==================================")


if __name__ == "__main__":
    main()