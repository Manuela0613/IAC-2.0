import requests

BASE_URL = "http://127.0.0.1:8000"


# ── Companies ─────────────────────────────

def get_companies():
    return requests.get(
        f"{BASE_URL}/companies/"
    ).json()


def create_company(data):
    return requests.post(
        f"{BASE_URL}/companies/",
        json=data
    ).json()


def update_company(company_id, data):
    return requests.patch(
        f"{BASE_URL}/companies/{company_id}",
        json=data
    ).json()


def delete_company(company_id):
    return requests.delete(
        f"{BASE_URL}/companies/{company_id}"
    ).json()


# ── Products ──────────────────────────────

def get_products():
    return requests.get(
        f"{BASE_URL}/products/"
    ).json()


def get_products_by_company(company_id):
    return requests.get(
        f"{BASE_URL}/products/company/{company_id}"
    ).json()


def create_product(data):
    return requests.post(
        f"{BASE_URL}/products/",
        json=data
    ).json()


def update_product(product_id, data):
    return requests.patch(
        f"{BASE_URL}/products/{product_id}",
        json=data
    ).json()


def delete_product(product_id):
    return requests.delete(
        f"{BASE_URL}/products/{product_id}"
    ).json()


# ── Services ──────────────────────────────

def get_services():
    return requests.get(
        f"{BASE_URL}/services/"
    ).json()


def get_services_by_company(company_id):
    return requests.get(
        f"{BASE_URL}/services/company/{company_id}"
    ).json()


def create_service(data):
    return requests.post(
        f"{BASE_URL}/services/",
        json=data
    ).json()


def update_service(service_id, data):
    return requests.patch(
        f"{BASE_URL}/services/{service_id}",
        json=data
    ).json()


def delete_service(service_id):
    return requests.delete(
        f"{BASE_URL}/services/{service_id}"
    ).json()