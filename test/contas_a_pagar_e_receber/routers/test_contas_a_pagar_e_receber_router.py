from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_dev_listar_contas_a_pagar_e_recber():
    response = client.get("/contas-a-pagar-e-receber")
    assert response.status_code == 200


def test_dev_criar_conta_a_pagar_e_receber():
    nova_conta = {
        "desc": "Curso Python",
        "valor": 123,
        "tipo": "pagar",
    }
    response = client.post("/contas-a-pagar-e-receber", json=nova_conta)
    assert response.status_code == 201