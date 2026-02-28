from fastapi import FastAPI

app = FastAPI(title="HRMS API")

@app.get("/")
def read_root():
    return {"status": "HRMS Backend Online"}