from app.jobs.repair_pending_job import execute


def main():
    try:
        execute()

    except Exception as e:
        print(f"[ERROR] {str(e)}")


if __name__ == "__main__":
    main()