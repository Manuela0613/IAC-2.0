import requests

BASE_URL = "http://127.0.0.1:8000"


def get_companies():
    return requests.get(f"{BASE_URL}/companies/").json()


def create_company(data):
    return requests.post(
        f"{BASE_URL}/companies/",
        json=data
    ).json()


def get_products():
    return requests.get(f"{BASE_URL}/products/").json()


def create_product(data):
    return requests.post(
        f"{BASE_URL}/products/",
        json=data
    ).json()


def get_services():
    return requests.get(f"{BASE_URL}/services/").json()


def create_service(data):
    return requests.post(
        f"{BASE_URL}/services/",
        json=data
    ).json()