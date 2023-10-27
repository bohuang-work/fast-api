import uvicorn
from fastapi import FastAPI
from internal.helper.app import build_fastapi_app
from internal.configs.config import load_app_config, AppConfig

app: FastAPI = build_fastapi_app()

if __name__ == "__main__":
    config: AppConfig = load_app_config()
    uvicorn.run(
        "main:app",
        host=config.host,
        port=config.port,
        reload=config.reload,
    )
