"""
Manejo global de excepciones HTTP.
"""

from fastapi import FastAPI
from fastapi.responses import JSONResponse

from src.core.exceptions import AppError


def register_exception_handlers(app: FastAPI) -> None:
    """Registra handlers globales."""

    @app.exception_handler(AppError)
    async def app_error_handler(_, exc: AppError):
        """Errores de dominio."""

        return JSONResponse(
            status_code=400,
            content={
                "detail": exc.message,
            },
        )

    @app.exception_handler(Exception)
    async def generic_error_handler(_, exc: Exception):
        """Errores inesperados."""

        return JSONResponse(
            status_code=500,
            content={
                "detail": str(exc),
            },
        )