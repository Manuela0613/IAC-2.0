"""
Endpoints HTTP para empresas.
"""

from fastapi import APIRouter, HTTPException, status

from src.core.exceptions import (
    DuplicateError,
    NotFoundError,
)

from src.schemas.company import (
    CompanyCreate,
    CompanyResponse,
    CompanyUpdate,
)

from src.services.company_service import (
    CompanyService,
)


router = APIRouter(
    prefix="/companies",
    tags=["Companies"],
)

service = CompanyService()


@router.get(
    "/",
    response_model=list[CompanyResponse],
)
def get_companies():
    """Lista todas las empresas."""
    return service.get_all_companies()


@router.get(
    "/{company_id}",
    response_model=CompanyResponse,
)
def get_company(company_id: int):
    """Obtiene empresa por ID."""

    try:
        return service.get_company_by_id(company_id)

    except NotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=exc.message,
        ) from exc


@router.post(
    "/",
    response_model=CompanyResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_company(payload: CompanyCreate):
    """Crea empresa."""

    try:
        return service.create_company(payload)

    except DuplicateError as exc:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=exc.message,
        ) from exc


@router.patch(
    "/{company_id}",
    response_model=CompanyResponse,
)
def update_company(
    company_id: int,
    payload: CompanyUpdate,
):
    """Actualiza empresa."""

    try:
        return service.update_company(
            company_id,
            payload,
        )

    except NotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=exc.message,
        ) from exc


@router.delete(
    "/{company_id}",
)
def delete_company(company_id: int):
    """Soft delete empresa."""

    try:
        return service.delete_company(company_id)

    except NotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=exc.message,
        ) from exc