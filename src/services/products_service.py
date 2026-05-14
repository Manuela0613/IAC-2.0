"""
Lógica de negocio para productos.
"""

from src.core.exceptions import (
    NotFoundError,
)

from src.schemas.product import (
    ProductCreate,
    ProductUpdate,
)

from src.storage.company_repository import (
    CompanyRepository,
)

from src.storage.product_repository import (
    ProductRepository,
)


class ProductService:
    """Casos de uso relacionados con productos."""

    def __init__(self) -> None:
        self.repository = ProductRepository()
        self.company_repository = CompanyRepository()

    # ── Consultas ──────────────────────────────────────────────────────────

    def get_all_products(self) -> list[dict]:
        """Lista todos los productos activos."""
        return self.repository.get_all()

    def get_product_by_id(self, product_id: int) -> dict:
        """Obtiene producto por ID."""

        product = self.repository.get_by_id(product_id)

        if not product:
            raise NotFoundError("Product", product_id)

        return product

    def get_products_by_company(
        self,
        company_id: int,
    ) -> list[dict]:
        """Lista productos de una empresa."""

        company = self.company_repository.get_by_id(company_id)

        if not company:
            raise NotFoundError("Company", company_id)

        return self.repository.get_by_company(company_id)

    # ── Escritura ──────────────────────────────────────────────────────────

    def create_product(self, payload: ProductCreate) -> dict:
        """Crea un producto."""

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

    def update_product(
        self,
        product_id: int,
        payload: ProductUpdate,
    ) -> dict:
        """Actualiza un producto."""

        product = self.repository.get_by_id(product_id)

        if not product:
            raise NotFoundError("Product", product_id)

        data = payload.model_dump(exclude_unset=True)

        return self.repository.update(product_id, data)

    def delete_product(self, product_id: int) -> dict:
        """Soft delete de producto."""

        product = self.repository.get_by_id(product_id)

        if not product:
            raise NotFoundError("Product", product_id)

        success = self.repository.delete(product_id)

        return {
            "success": success,
            "message": "Producto desactivado correctamente.",
        }