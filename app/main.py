from app.jobs.job_registry import JOB_REGISTRY


def main():

    job_name = "repair_pending"

    job = JOB_REGISTRY[job_name]()

    result = job.execute()

    print()
    print("==================================")
    print(f"JOB          : {result.job_name}")
    print(f"TOTAL ROWS   : {result.total_rows}")
    print(f"FILTERED     : {result.filtered_rows}")
    print(f"VENDORS      : {result.vendor_count}")
    print(f"OUTPUT FILES : {result.output_file_count}")
    print(f"ZIP FILE     : {result.zip_file_path}")
    print(f"SUCCESS      : {result.success}")
    print(f"MESSAGE      : {result.message}")
    print("==================================")


if __name__ == "__main__":
    main()