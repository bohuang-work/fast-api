from fastapi import FastAPI

from internal.handlers import health, player


def build_fastapi_app() -> FastAPI:
    fastapi_app: FastAPI = FastAPI(
        title="NBA Players",
        description="API for NBA Players",
    )

    # Add routes
    fastapi_app.include_router(health.router, tags=["Health"])
    fastapi_app.include_router(player.router, tags=["Players"])

    return fastapi_app
