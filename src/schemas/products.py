"""
Schemas Pydantic para la entidad Product.
"""

from decimal import Decimal

from pydantic import BaseModel, Field, field_validator, model_validator


class ProductBase(BaseModel):
    """Campos comunes de Product."""

    company_id: int = Field(
        ...,
        gt=0,
        description="Empresa propietaria del producto.",
        examples=[1],
    )

    name: str = Field(
        ...,
        min_length=2,
        max_length=100,
        description="Nombre del producto.",
        examples=["Laptop"],
    )

    price: Decimal = Field(
        ...,
        decimal_places=2,
        description="Precio del producto.",
        examples=[2500.00],
    )

    stock: int = Field(
        ...,
        ge=0,
        description="Cantidad disponible en inventario.",
        examples=[5],
    )

    # ── Validaciones ──────────────────────────────────────────────────────

    @field_validator("price")
    @classmethod
    def price_must_be_positive(cls, value: Decimal) -> Decimal:
        """El precio debe ser mayor que 0."""
        if value <= 0:
            raise ValueError("El precio debe ser mayor que 0.")
        return value


# ── Create ────────────────────────────────────────────────────────────────

class ProductCreate(ProductBase):
    """Payload para crear un producto."""


# ── Update ────────────────────────────────────────────────────────────────

class ProductUpdate(BaseModel):
    """Payload para actualizar un producto."""

    name: str | None = Field(
        default=None,
        min_length=2,
        max_length=100,
    )

    price: Decimal | None = Field(
        default=None,
        decimal_places=2,
    )

    stock: int | None = Field(
        default=None,
        ge=0,
    )

    @field_validator("price")
    @classmethod
    def price_must_be_positive(cls, value: Decimal | None) -> Decimal | None:
        if value is not None and value <= 0:
            raise ValueError("El precio debe ser mayor que 0.")
        return value

    @model_validator(mode="after")
    def at_least_one_field(self) -> "ProductUpdate":
        """Obliga a enviar al menos un campo."""
        if (
            self.name is None
            and self.price is None
            and self.stock is None
        ):
            raise ValueError(
                "Debes enviar al menos un campo para actualizar."
            )
        return self


# ── Response ──────────────────────────────────────────────────────────────

class ProductResponse(ProductBase):
    """Respuesta de Product enviada por la API."""

    id: int = Field(
        ...,
        description="ID único del producto.",
    )

    is_active: bool = Field(
        ...,
        description="Indica si el producto está activo.",
    )

    model_config = {"from_attributes": True}