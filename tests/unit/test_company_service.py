from src.services.company_service import CompanyService


def test_company_service_exists():
    service = CompanyService()

    assert service is not None