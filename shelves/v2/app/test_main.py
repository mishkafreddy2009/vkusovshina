from fastapi.testclient import TestClient
from main import app
# import pytest
# from httpx import AsyncClient


client = TestClient(app)


def test_read_homepage():
    response = client.get("/api/v1/home/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello, World!"}


def test_create_shelf():
    response = client.post(
        "/api/v1/shelves/",
        json = {
            "name": "Candies",
            "description": "Shelf of 10 products specified for candies",
            "capacity": 10,
            "current_stock": 0,
            "is_full": False
        }
    )
    assert response.status_code == 200
    assert response.json() == {
        "name": "Candies",
        "description": "Shelf of 10 products specified for candies",
        "capacity": 10,
        "current_stock": 0,
        "is_full": False,
        "id": 1
    }


# def test_read_shelves():
#     client.post(
#         "/api/v1/shelves/",
#         json = {
#             "name": "Candies",
#             "description": "Shelf of 10 products specified for candies",
#             "capacity": 10,
#             "current_stock": 0,
#             "is_full": False
#         }
#     )
#     client.post(
#         "/api/v1/shelves/",
#         json = {
#             "name": "Bread",
#             "description": "Shelf of 20 products specified for bread",
#             "capacity": 20,
#             "current_stock": 0,
#             "is_full": False
#         }
#     )
#     response = client.get("/api/v1/shelves/")
#     assert response.status_code == 200
#     assert response.json() == [
#         {
#             "name": "Candies",
#             "description": "Shelf of 10 products specified for candies",
#             "capacity": 10,
#             "current_stock": 0,
#             "is_full": False,
#             "id": 1
#         },
#         {
#             "name": "Bread",
#             "description": "Shelf of 20 products specified for bread",
#             "capacity": 20,
#             "current_stock": 0,
#             "is_full": False,
#             "id": 2
#         }
#     ]


# def test_update_shelf():
#     client.post("/api/v1/shelves/",
#         json = {
#             "name": "Candies",
#             "description": "Shelf of 10 products specified for candies",
#             "capacity": 10,
#             "current_stock": 0,
#             "is_full": False
#         }
#     )
#     response = client.put(
#         "/api/v1/shelves/1",
#         json = {
#             "name": "Bread",
#             "description": "Shelf of 20 products specified for bread",
#             "capacity": 20,
#             "current_stock": 0,
#             "is_full": False,
#         }
#     )
#     assert response.status_code == 200
#     assert response.json() == {
#         "name": "Bread",
#         "description": "Shelf of 20 products specified for bread",
#         "capacity": 20,
#         "current_stock": 0,
#         "is_full": False,
#         "id": 1
#     }


# post instead of post+put -> 405 error
def test_update_shelf_method_not_allowed():
    response = client.post(
        "/api/v1/shelves/1/",
        json = {
            "name": "Bread",
            "description": "Shelf of 20 products specified for bread",
            "capacity": 20,
            "current_stock": 0,
            "is_full": False,
            "id": 1
        }
    )
    assert response.status_code == 405
    assert response.json() == {"detail": "Method Not Allowed"}