"""
Schemas Pydantic para la entidad Company.
"""

from pydantic import BaseModel, Field, field_validator, model_validator


class CompanyBase(BaseModel):
    """Campos comunes de Company."""

    name: str = Field(
        ...,
        min_length=2,
        max_length=100,
        description="Nombre de la empresa.",
        examples=["IAC SAS"],
    )

    nit: str = Field(
        ...,
        min_length=5,
        max_length=20,
        description="NIT único de la empresa.",
        examples=["900123456"],
    )

    # ── Validaciones ──────────────────────────────────────────────────────

    @field_validator("nit")
    @classmethod
    def nit_must_be_numeric(cls, value: str) -> str:
        """Valida que el NIT solo tenga números."""
        if not value.isdigit():
            raise ValueError("El NIT debe contener solo números.")
        return value


# ── Create ────────────────────────────────────────────────────────────────

class CompanyCreate(CompanyBase):
    """Payload para crear una empresa."""


# ── Update ────────────────────────────────────────────────────────────────

class CompanyUpdate(BaseModel):
    """Payload para actualizar una empresa."""

    name: str | None = Field(
        default=None,
        min_length=2,
        max_length=100,
    )

    nit: str | None = Field(
        default=None,
        min_length=5,
        max_length=20,
    )

    @field_validator("nit")
    @classmethod
    def nit_must_be_numeric(cls, value: str | None) -> str | None:
        if value is not None and not value.isdigit():
            raise ValueError("El NIT debe contener solo números.")
        return value

    @model_validator(mode="after")
    def at_least_one_field(self) -> "CompanyUpdate":
        """Obliga a enviar al menos un campo."""
        if self.name is None and self.nit is None:
            raise ValueError(
                "Debes enviar al menos un campo para actualizar."
            )
        return self


# ── Response ──────────────────────────────────────────────────────────────

class CompanyResponse(CompanyBase):
    """Respuesta de Company enviada por la API."""

    id: int = Field(
        ...,
        description="ID único de la empresa.",
    )

    is_active: bool = Field(
        ...,
        description="Indica si la empresa está activa.",
    )

    model_config = {"from_attributes": True}