from fastapi import FastAPI
from internal.handlers import health


def build_fastapi_app() -> FastAPI:
    fastapi_app: FastAPI = FastAPI(
        title="NBA Players",
        description="API for NBA Players",
    )

    # Add routes
    fastapi_app.include_router(health.router, tags=["Health"])
    return fastapi_app
