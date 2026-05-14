"""
Lógica de negocio para servicios.
"""

from src.core.exceptions import (
    NotFoundError,
)

from src.schemas.service import (
    ServiceCreate,
    ServiceUpdate,
)

from src.storage.company_repository import (
    CompanyRepository,
)

from src.storage.service_repository import (
    ServiceRepository,
)


class ServiceService:
    """Casos de uso relacionados con servicios."""

    def __init__(self) -> None:
        self.repository = ServiceRepository()
        self.company_repository = CompanyRepository()

    # ── Consultas ──────────────────────────────────────────────────────────

    def get_all_services(self) -> list[dict]:
        """Lista todos los servicios activos."""
        return self.repository.get_all()

    def get_service_by_id(self, service_id: int) -> dict:
        """Obtiene servicio por ID."""

        service = self.repository.get_by_id(service_id)

        if not service:
            raise NotFoundError("Service", service_id)

        return service

    def get_services_by_company(
        self,
        company_id: int,
    ) -> list[dict]:
        """Lista servicios de una empresa."""

        company = self.company_repository.get_by_id(company_id)

        if not company:
            raise NotFoundError("Company", company_id)

        return self.repository.get_by_company(company_id)

    # ── Escritura ──────────────────────────────────────────────────────────

    def create_service(self, payload: ServiceCreate) -> dict:
        """Crea un servicio."""

        company = self.company_repository.get_by_id(
            payload.company_id
        )

        if not company:
            raise NotFoundError(
                "Company",
                payload.company_id,
            )

        data = payload.model_dump()

        data["is_active"] = True

        return self.repository.create(data)

    def update_service(
        self,
        service_id: int,
        payload: ServiceUpdate,
    ) -> dict:
        """Actualiza un servicio."""

        service = self.repository.get_by_id(service_id)

        if not service:
            raise NotFoundError("Service", service_id)

        data = payload.model_dump(exclude_unset=True)

        return self.repository.update(service_id, data)

    def delete_service(self, service_id: int) -> dict:
        """Soft delete de servicio."""

        service = self.repository.get_by_id(service_id)

        if not service:
            raise NotFoundError("Service", service_id)

        success = self.repository.delete(service_id)

        return {
            "success": success,
            "message": "Servicio desactivado correctamente.",
        }