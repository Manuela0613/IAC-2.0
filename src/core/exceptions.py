"""
Excepciones de dominio de la aplicación.

Estas excepciones representan errores de negocio y son independientes
de FastAPI, Supabase o cualquier otro framework.
"""


class AppError(Exception):
    """Clase base para todas las excepciones del sistema."""

    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(message)


# ── Not Found ──────────────────────────────────────────────────────────────

class NotFoundError(AppError):
    """Se lanza cuando un recurso no existe."""

    def __init__(self, resource: str, identifier: int | str) -> None:
        super().__init__(
            f"{resource} con id={identifier!r} no encontrado."
        )


# ── Duplicate ──────────────────────────────────────────────────────────────

class DuplicateError(AppError):
    """Se lanza cuando ya existe un recurso duplicado."""

    def __init__(self, resource: str, field: str, value: str) -> None:
        super().__init__(
            f"{resource} con {field}={value!r} ya existe."
        )


# ── Validation ─────────────────────────────────────────────────────────────

class ValidationError(AppError):
    """Se lanza cuando una regla de negocio no se cumple."""

    def __init__(self, message: str) -> None:
        super().__init__(message)


# ── Storage ────────────────────────────────────────────────────────────────

class StorageError(AppError):
    """Errores relacionados con Supabase o persistencia."""

    def __init__(self, operation: str, detail: str) -> None:
        super().__init__(
            f"Error de almacenamiento en '{operation}': {detail}"
        )