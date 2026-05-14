"""
Endpoints HTTP para productos.
"""

from fastapi import APIRouter, HTTPException, status

from src.core.exceptions import (
    NotFoundError,
)

from src.schemas.product import (
    ProductCreate,
    ProductResponse,
    ProductUpdate,
)

from src.services.product_service import (
    ProductService,
)


router = APIRouter(
    prefix="/products",
    tags=["Products"],
)

service = ProductService()


@router.get(
    "/",
    response_model=list[ProductResponse],
)
def get_products():
    """Lista productos."""
    return service.get_all_products()


@router.get(
    "/{product_id}",
    response_model=ProductResponse,
)
def get_product(product_id: int):
    """Obtiene producto por ID."""

    try:
        return service.get_product_by_id(product_id)

    except NotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=exc.message,
        ) from exc


@router.get(
    "/company/{company_id}",
    response_model=list[ProductResponse],
)
def get_products_by_company(company_id: int):
    """Lista productos de una empresa."""

    try:
        return service.get_products_by_company(company_id)

    except NotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=exc.message,
        ) from exc


@router.post(
    "/",
    response_model=ProductResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_product(payload: ProductCreate):
    """Crea producto."""

    try:
        return service.create_product(payload)

    except NotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=exc.message,
        ) from exc


@router.patch(
    "/{product_id}",
    response_model=ProductResponse,
)
def update_product(
    product_id: int,
    payload: ProductUpdate,
):
    """Actualiza producto."""

    try:
        return service.update_product(
            product_id,
            payload,
        )

    except NotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=exc.message,
        ) from exc


@router.delete(
    "/{product_id}",
)
def delete_product(product_id: int):
    """Soft delete producto."""

    try:
        return service.delete_product(product_id)

    except NotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=exc.message,
        ) from exc