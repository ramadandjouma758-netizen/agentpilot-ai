from fastapi import FastAPI

app = FastAPI(
    title="AgentPilot AI",
    description="AI-powered automation platform",
    version="0.1.0",
)


@app.get("/")
def root():
    return {"message": "AgentPilot AI API is running"}
