from fastapi import FastAPI

app = FastAPI(
    title="Automation Runtime",
    version="0.4.0"
)


@app.get("/")
def root():
    return {
        "message": "Automation Runtime"
    }
