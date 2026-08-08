from fastapi import FastAPI

from routes import router as users_router

app = FastAPI(
    title="AgentPilot AI",
    description="AI-powered automation platform",
    version="0.1.0",
)

app.include_router(users_router)


@app.get("/")
def root():
    return {"message": "AgentPilot AI API is running"}
