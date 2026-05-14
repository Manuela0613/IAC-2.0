"""
Repositorio de servicios.
"""

from src.storage.base import BaseRepository


class ServiceRepository(BaseRepository):
    """Acceso a datos para la tabla services."""

    TABLE = "services"

    # ── Consultas ──────────────────────────────────────────────────────────

    def get_all(self) -> list[dict]:
        """Retorna todos los servicios activos."""

        response = self._execute(
            "service.get_all",
            lambda: self.client.table(self.TABLE)
            .select("*")
            .eq("is_active", True)
            .order("id")
            .execute(),
        )

        return response.data or []

    def get_by_id(self, service_id: int) -> dict | None:
        """Busca servicio por ID."""

        response = self._execute(
            "service.get_by_id",
            lambda: self.client.table(self.TABLE)
            .select("*")
            .eq("id", service_id)
            .eq("is_active", True)
            .execute(),
        )

        data: list[dict] = response.data or []

        return data[0] if data else None

    def get_by_company(self, company_id: int) -> list[dict]:
        """Lista servicios de una empresa."""

        response = self._execute(
            "service.get_by_company",
            lambda: self.client.table(self.TABLE)
            .select("*")
            .eq("company_id", company_id)
            .eq("is_active", True)
            .execute(),
        )

        return response.data or []

    # ── Escritura ──────────────────────────────────────────────────────────

    def create(self, data: dict) -> dict:
        """Crea un servicio."""

        response = self._execute(
            "service.create",
            lambda: self.client.table(self.TABLE)
            .insert(data)
            .execute(),
        )

        return self._require_data(response, "service.create")[0]

    def update(self, service_id: int, data: dict) -> dict:
        """Actualiza un servicio."""

        response = self._execute(
            "service.update",
            lambda: self.client.table(self.TABLE)
            .update(data)
            .eq("id", service_id)
            .execute(),
        )

        return self._require_data(response, "service.update")[0]

    def delete(self, service_id: int) -> bool:
        """Soft delete de servicio."""

        response = self._execute(
            "service.delete",
            lambda: self.client.table(self.TABLE)
            .update({"is_active": False})
            .eq("id", service_id)
            .execute(),
        )

        data: list[dict] = response.data or []

        return len(data) > 0