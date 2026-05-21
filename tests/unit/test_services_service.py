from src.services.service_service import ServiceService


def test_services_service_exists():
    service = ServiceService()

    assert service is not None