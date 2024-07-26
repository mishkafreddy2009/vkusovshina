import time

from httpx import AsyncClient
from sqlalchemy import insert, select

from src.auth.auth import auth_backend
from src.models import role
from src.router import current_user
from tests.conftest import async_session_maker, client


async def test_customers(ac: AsyncClient):
    response = await ac.get("/customers")

    assert response.status_code == 200


async def test_products(ac: AsyncClient):
    response = await ac.get("/products")

    assert response.status_code == 200

async def test_baskets(ac: AsyncClient):
    response = await ac.get("/baskets")

    assert response.status_code == 200

async def test_purchases_123(ac: AsyncClient):
    response = await ac.get("/purchases/123")

    assert response.status_code == 200


async def test_add_product(ac: AsyncClient):

    response = await ac.post("/products", json={
        "category": "zzz",
        "quantity": 10,
        "price": 1
    })
    assert response.status_code == 200

async def test_add_role():
    async with async_session_maker() as session:
        stmt = insert(role).values(id=1, name="admin", permissions=None)
        await session.execute(stmt)
        await session.commit()

        query = select(role)
        result = await session.execute(query)
        assert result.all() == [(1, 'admin', None)], "Роль не добавилась"


async def test_register(ac: AsyncClient):
    response = await ac.post("/auth/register", json={
      "email": "Vasa",
      "password": "Vasa",
      "is_active": True,
      "is_superuser": False,
      "is_verified": False,
      "username": "Vasa123",
      "role_id": 1
    })
    ac.cookies = response.cookies
    assert response.status_code == 201


async def test_login(ac: AsyncClient):
    response = await ac.post("/auth/jwt/login", data={
        "grant_type": "",
        "username": "Vasa",
        "password": "Vasa",
        "scope": "",
        "client_id": "",
        "client_secret": ""
    }, headers={
        "Content-Type": "application/x-www-form-urlencoded"
    })

    ac.cookies = response.cookies
    assert response.status_code == 204



async def test_add_to_basket(ac: AsyncClient):
    response1 = await ac.post("/auth/jwt/login", data={
        "grant_type": None,
        "username": "Vasa",
        "password": "Vasa",
        "scope": None,
        "client_id": None,
        "client_secret": None
    }, headers={
        "Content-Type": "application/x-www-form-urlencoded"
    }) #json надо сделать
    assert response1.status_code == 204
    gg = auth_backend.get_strategy
    print("?????????????????????????????/", gg)
    response2 = await ac.post("/baskets", json={
        "category": "qwe",
        "quantity": 5
    })
    print("#################################Auth response headers:", response2.headers)
    assert response2.status_code == 200


async def test_comlete_purchase(ac: AsyncClient):
    response = await ac.post("/purchases")

    assert response.status_code == 200
