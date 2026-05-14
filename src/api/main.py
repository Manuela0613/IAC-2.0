"""
Entrypoint principal de FastAPI.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api.routers.company import router as company_router
from src.core.config import settings
from src.api.routers.product import router as products_router
from src.api.routers.service     import router as service_router
from src.api.dependencies import register_exception_handlers



app = FastAPI(
    title=settings.api_title,
    version=settings.api_version,
)

app.include_router(company_router)
app.include_router(products_router)
app.include_router(service_router)
register_exception_handlers(app)
# ── CORS ──────────────────────────────────────────────────────────────────

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ── Root endpoint ─────────────────────────────────────────────────────────

@app.get("/")
def root() -> dict:
    """Endpoint base."""
    return {
        "message": "IAC API funcionando correctamente 🚀"
    }