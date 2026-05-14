"""
Lógica de negocio para empresas.
"""

from src.core.exceptions import (
    DuplicateError,
    NotFoundError,
)

from src.schemas.company import (
    CompanyCreate,
    CompanyUpdate,
)

from src.storage.company_repository import (
    CompanyRepository,
)


class CompanyService:
    """Casos de uso relacionados con empresas."""

    def __init__(self) -> None:
        self.repository = CompanyRepository()

    # ── Consultas ──────────────────────────────────────────────────────────

    def get_all_companies(self) -> list[dict]:
        """Lista todas las empresas activas."""
        return self.repository.get_all()

    def get_company_by_id(self, company_id: int) -> dict:
        """Obtiene empresa por ID."""

        company = self.repository.get_by_id(company_id)

        if not company:
            raise NotFoundError("Company", company_id)

        return company

    # ── Escritura ──────────────────────────────────────────────────────────

    def create_company(self, payload: CompanyCreate) -> dict:
        """Crea una empresa validando duplicados."""

        existing_company = self.repository.get_by_nit(payload.nit)

        if existing_company:
            raise DuplicateError(
                "Company",
                "nit",
                payload.nit,
            )

        data = payload.model_dump()

        data["is_active"] = True

        return self.repository.create(data)

    def update_company(
        self,
        company_id: int,
        payload: CompanyUpdate,
    ) -> dict:
        """Actualiza una empresa."""

        company = self.repository.get_by_id(company_id)

        if not company:
            raise NotFoundError("Company", company_id)

        data = payload.model_dump(exclude_unset=True)

        return self.repository.update(company_id, data)

    def delete_company(self, company_id: int) -> dict:
        """Soft delete de empresa."""

        company = self.repository.get_by_id(company_id)

        if not company:
            raise NotFoundError("Company", company_id)

        success = self.repository.delete(company_id)

        return {
            "success": success,
            "message": "Empresa desactivada correctamente.",
        }