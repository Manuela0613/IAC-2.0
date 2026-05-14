"""
Repositorio base para Supabase.

Centraliza:
- conexión con Supabase,
- manejo de errores,
- helpers comunes para repositories.
"""

from collections.abc import Callable
from typing import Any, TypeVar

from supabase import Client, create_client

from src.core.config import settings
from src.core.exceptions import StorageError

T = TypeVar("T")


class BaseRepository:
    """Clase base que heredarán todos los repositories."""

    def __init__(self) -> None:
        self.client: Client = create_client(
            settings.supabase_url,
            settings.supabase_key,
        )

    # ── Helpers internos ──────────────────────────────────────────────────

    def _execute(self, operation: str, fn: Callable[[], Any]) -> Any:
        """
        Ejecuta operaciones de Supabase manejando errores uniformemente.
        """
        try:
            return fn()

        except StorageError:
            raise

        except Exception as exc:
            raise StorageError(
                operation=operation,
                detail=str(exc),
            ) from exc

    @staticmethod
    def _require_data(response: Any, operation: str) -> list[dict]:
        """
        Verifica que Supabase haya retornado datos válidos.
        """
        data: list[dict] | None = getattr(response, "data", None)

        if not data:
            raise StorageError(
                operation=operation,
                detail="La operación no retornó datos.",
            )

        return data
