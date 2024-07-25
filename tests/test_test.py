import time

from httpx import AsyncClient
from sqlalchemy import insert, select

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
        "category": "qwe",
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
    async with async_session_maker() as session:
        response = await ac.post("/auth/register", json={
          "email": "string",
          "password": "string",
          "is_active": True,
          "is_superuser": False,
          "is_verified": False,
          "username": "string",
          "role_id": 0
        })

    assert response.status_code == 204

async def test_login(ac: AsyncClient):
    response = await ac.post("/auth/jwt/login", data={
        "grant_type": "",
        "username": "zxc",
        "password": "zxc",
        "scope": "",
        "client_id": "",
        "client_secret": ""
    }, headers={
        "Content-Type": "application/x-www-form-urlencoded"
    })
    assert response.status_code == 204
    return response.cookies



async def test_add_to_basket(ac: AsyncClient):
    # Аутентификация и получение токена
    auth_response = await ac.post("/auth/jwt/login", data={
        "grant_type": "",
        "username": "zxc",
        "password": "zxc",
        "scope": "",
        "client_id": "",
        "client_secret": ""
    }, headers={
        "Content-Type": "application/x-www-form-urlencoded"
    })
    # Вывод для отладки
    print("#################################Auth response status:", auth_response.status_code)
    #print("#################################Auth response text:", auth_response.json())
    print("#################################Auth response headers:", auth_response.cookies)
    print("#################################Auth response headers:", auth_response.headers.get("set-cookie"))
    # Проверка успешности аутентификации
    assert auth_response.status_code == 204  # или соответствующий код успешной аутентификации

    # Получение токена из ответа
    #auth_data = auth_response.json()
    # token = auth_data.get("access_token")
    # assert token is not None, "Access token not found in the response"

    # Использование токена для запроса к /baskets
    response = await ac.post("/baskets", json={
        "category": "qwe",
        "quantity": 5
    })
    print("#################################Auth response headers:", response.headers)
    assert response.status_code == 200


async def test_comlete_purchase(ac: AsyncClient):
    response = await ac.post("/purchases")
    time.sleep(10)
    assert response.status_code == 200
