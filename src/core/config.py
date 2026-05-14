"""
Configuración central de la aplicación.

Usa pydantic-settings para leer variables de entorno desde el archivo .env.
Se instancia una sola vez como singleton (settings) y se importa
desde cualquier módulo que lo necesite.
"""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Variables de entorno validadas y tipadas."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )

    # ── Supabase ──────────────────────────────────────────────────────────

    supabase_url: str
    supabase_key: str

    # ── FastAPI ───────────────────────────────────────────────────────────

    api_base_url: str = "http://localhost:8000"
    api_title: str = "IAC API"
    api_version: str = "1.0.0"

    # ── Entorno ───────────────────────────────────────────────────────────

    debug: bool = True


# Singleton global
settings = Settings()