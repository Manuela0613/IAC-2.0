"""
Repositorio de empresas.

Esta capa:
- SOLO habla con Supabase.
- NO contiene lógica de negocio.
- SOLO hace operaciones CRUD.
"""

from src.storage.base import BaseRepository


class CompanyRepository(BaseRepository):
    """Acceso a datos para la tabla companies."""

    TABLE = "companies"

    # ── Consultas ──────────────────────────────────────────────────────────

    def get_all(self) -> list[dict]:
        """Retorna todas las empresas activas."""

        response = self._execute(
            "company.get_all",
            lambda: self.client.table(self.TABLE)
            .select("*")
            .eq("is_active", True)
            .order("id")
            .execute(),
        )

        return response.data or []

    def get_by_id(self, company_id: int) -> dict | None:
        """Retorna una empresa activa por ID."""

        response = self._execute(
            "company.get_by_id",
            lambda: self.client.table(self.TABLE)
            .select("*")
            .eq("id", company_id)
            .eq("is_active", True)
            .execute(),
        )

        data: list[dict] = response.data or []

        return data[0] if data else None

    def get_by_nit(self, nit: str) -> dict | None:
        """Busca empresa por NIT."""

        response = self._execute(
            "company.get_by_nit",
            lambda: self.client.table(self.TABLE)
            .select("*")
            .eq("nit", nit)
            .eq("is_active", True)
            .execute(),
        )

        data: list[dict] = response.data or []

        return data[0] if data else None

    # ── Escritura ──────────────────────────────────────────────────────────

    def create(self, data: dict) -> dict:
        """Crea una nueva empresa."""

        response = self._execute(
            "company.create",
            lambda: self.client.table(self.TABLE)
            .insert(data)
            .execute(),
        )

        return self._require_data(response, "company.create")[0]

    def update(self, company_id: int, data: dict) -> dict:
        """Actualiza una empresa."""

        response = self._execute(
            "company.update",
            lambda: self.client.table(self.TABLE)
            .update(data)
            .eq("id", company_id)
            .execute(),
        )

        return self._require_data(response, "company.update")[0]

    def delete(self, company_id: int) -> bool:
        """
        Soft delete:
        NO elimina realmente la empresa.
        """

        response = self._execute(
            "company.delete",
            lambda: self.client.table(self.TABLE)
            .update({"is_active": False})
            .eq("id", company_id)
            .execute(),
        )

        data: list[dict] = response.data or []

        return len(data) > 0