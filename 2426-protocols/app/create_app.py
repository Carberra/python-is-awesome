from typing import Protocol

from starlette.applications import Starlette
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse
from starlette.routing import Route


class Config(Protocol):
    CONFIGURE_MIDDLEWARE: bool
    SERVICE_NAME: str


def create_app(config: Config) -> Starlette:
    app = Starlette(
        routes=[
            Route(
                f"{config.SERVICE_NAME}/hello",
                endpoint=lambda _: JSONResponse({"hello": "world"}),
                methods=["GET"],
            ),
        ]
    )

    if config.CONFIGURE_MIDDLEWARE:
        app.add_middleware(CORSMiddleware, allow_origins=["*"])

    return app
