from src.services.product_service import ProductService


def test_products_service_exists():
    service = ProductService()

    assert service is not None