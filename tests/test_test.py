from httpx import AsyncClient

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
    response = await ac.post("/products?category=%D0%BF%D0%B8%D0%B2%D0%BE&quantity=10&price=1.99")
    assert response.status_code == 200

async def test_login(ac: AsyncClient):
    response = await ac.post("/auth/jwt/login")
    assert response.status_code == 204


async def test_add_to_basket(ac: AsyncClient):
    response = await ac.post("/baskets?pr_category=%D0%BF%D0%B8%D0%B2%D0%BE&quantity=5")
    assert response.status_code == 200