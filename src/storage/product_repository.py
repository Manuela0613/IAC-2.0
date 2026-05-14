"""
Repositorio de productos.
"""

from src.storage.base import BaseRepository


class ProductRepository(BaseRepository):
    """Acceso a datos para la tabla products."""

    TABLE = "products"

    # ── Consultas ──────────────────────────────────────────────────────────

    def get_all(self) -> list[dict]:
        """Retorna todos los productos activos."""

        response = self._execute(
            "product.get_all",
            lambda: self.client.table(self.TABLE)
            .select("*")
            .eq("is_active", True)
            .order("id")
            .execute(),
        )

        return response.data or []

    def get_by_id(self, product_id: int) -> dict | None:
        """Busca producto por ID."""

        response = self._execute(
            "product.get_by_id",
            lambda: self.client.table(self.TABLE)
            .select("*")
            .eq("id", product_id)
            .eq("is_active", True)
            .execute(),
        )

        data: list[dict] = response.data or []

        return data[0] if data else None

    def get_by_company(self, company_id: int) -> list[dict]:
        """Lista productos de una empresa."""

        response = self._execute(
            "product.get_by_company",
            lambda: self.client.table(self.TABLE)
            .select("*")
            .eq("company_id", company_id)
            .eq("is_active", True)
            .execute(),
        )

        return response.data or []

    # ── Escritura ──────────────────────────────────────────────────────────

    def create(self, data: dict) -> dict:
        """Crea un producto."""

        response = self._execute(
            "product.create",
            lambda: self.client.table(self.TABLE)
            .insert(data)
            .execute(),
        )

        return self._require_data(response, "product.create")[0]

    def update(self, product_id: int, data: dict) -> dict:
        """Actualiza un producto."""

        response = self._execute(
            "product.update",
            lambda: self.client.table(self.TABLE)
            .update(data)
            .eq("id", product_id)
            .execute(),
        )

        return self._require_data(response, "product.update")[0]

    def delete(self, product_id: int) -> bool:
        """Soft delete de producto."""

        response = self._execute(
            "product.delete",
            lambda: self.client.table(self.TABLE)
            .update({"is_active": False})
            .eq("id", product_id)
            .execute(),
        )

        data: list[dict] = response.data or []

        return len(data) > 0