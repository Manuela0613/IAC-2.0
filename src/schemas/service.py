"""
Schemas Pydantic para la entidad Service.
"""

from decimal import Decimal

from pydantic import BaseModel, Field, field_validator, model_validator


class ServiceBase(BaseModel):
    """Campos comunes de Service."""

    company_id: int = Field(
        ...,
        gt=0,
        description="Empresa propietaria del servicio.",
        examples=[1],
    )

    name: str = Field(
        ...,
        min_length=2,
        max_length=100,
        description="Nombre del servicio.",
        examples=["Consultoría"],
    )

    description: str = Field(
        ...,
        min_length=5,
        max_length=500,
        description="Descripción del servicio.",
        examples=["Servicio empresarial de consultoría."],
    )

    price: Decimal = Field(
        ...,
        decimal_places=2,
        description="Precio del servicio.",
        examples=[500.00],
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

class ServiceCreate(ServiceBase):
    """Payload para crear un servicio."""


# ── Update ────────────────────────────────────────────────────────────────

class ServiceUpdate(BaseModel):
    """Payload para actualizar un servicio."""

    name: str | None = Field(
        default=None,
        min_length=2,
        max_length=100,
    )

    description: str | None = Field(
        default=None,
        min_length=5,
        max_length=500,
    )

    price: Decimal | None = Field(
        default=None,
        decimal_places=2,
    )

    @field_validator("price")
    @classmethod
    def price_must_be_positive(cls, value: Decimal | None) -> Decimal | None:
        if value is not None and value <= 0:
            raise ValueError("El precio debe ser mayor que 0.")
        return value

    @model_validator(mode="after")
    def at_least_one_field(self) -> "ServiceUpdate":
        """Obliga a enviar al menos un campo."""
        if (
            self.name is None
            and self.description is None
            and self.price is None
        ):
            raise ValueError(
                "Debes enviar al menos un campo para actualizar."
            )
        return self


# ── Response ──────────────────────────────────────────────────────────────

class ServiceResponse(ServiceBase):
    """Respuesta de Service enviada por la API."""

    id: int = Field(
        ...,
        description="ID único del servicio.",
    )

    is_active: bool = Field(
        ...,
        description="Indica si el servicio está activo.",
    )

    model_config = {"from_attributes": True}