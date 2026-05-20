from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_listar_usuarios():

    response = client.get("/usuarios")

    assert response.status_code == 200