"""
Endpoints HTTP para servicios.
"""

from fastapi import APIRouter, HTTPException, status

from src.core.exceptions import (
    NotFoundError,
)

from src.schemas.service import (
    ServiceCreate,
    ServiceResponse,
    ServiceUpdate,
)

from src.services.service_service import (
    ServiceService,
)


router = APIRouter(
    prefix="/services",
    tags=["Services"],
)

service = ServiceService()


@router.get(
    "/",
    response_model=list[ServiceResponse],
)
def get_services():
    """Lista servicios."""
    return service.get_all_services()


@router.get(
    "/{service_id}",
    response_model=ServiceResponse,
)
def get_service(service_id: int):
    """Obtiene servicio por ID."""

    try:
        return service.get_service_by_id(service_id)

    except NotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=exc.message,
        ) from exc


@router.get(
    "/company/{company_id}",
    response_model=list[ServiceResponse],
)
def get_services_by_company(company_id: int):
    """Lista servicios de una empresa."""

    try:
        return service.get_services_by_company(company_id)

    except NotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=exc.message,
        ) from exc


@router.post(
    "/",
    response_model=ServiceResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_service(payload: ServiceCreate):
    """Crea servicio."""

    try:
        return service.create_service(payload)

    except NotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=exc.message,
        ) from exc


@router.patch(
    "/{service_id}",
    response_model=ServiceResponse,
)
def update_service(
    service_id: int,
    payload: ServiceUpdate,
):
    """Actualiza servicio."""

    try:
        return service.update_service(
            service_id,
            payload,
        )

    except NotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=exc.message,
        ) from exc


@router.delete(
    "/{service_id}",
)
def delete_service(service_id: int):
    """Soft delete servicio."""

    try:
        return service.delete_service(service_id)

    except NotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=exc.message,
        ) from exc