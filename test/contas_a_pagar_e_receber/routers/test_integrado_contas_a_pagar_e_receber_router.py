from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from main import app
from sqlalchemy.orm import sessionmaker

from shared.dependencies import get_db
from shared.database import Base

client = TestClient(app)

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}
)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

def test_dev_listar_contas_a_pagar_e_receber():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    client.get("/contas-a-pagar-e-receber", json={"desc":"Aluguel", "valor": 1000, "tipo":"pagar"})
    response = client.get("/contas-a-pagar-e-receber")
    assert response.status_code == 200
    # assert response.json() == []


def test_dev_criar_conta_a_pagar_e_receber():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    client.post("/contas-a-pagar-e-receber")
    nova_conta = {
        "desc": "Curso Python",
        "valor": 123,
        "tipo": "pagar",
    }
    nova_conta_copy = nova_conta.copy()
    nova_conta_copy["id"] = 1
    response = client.post("/contas-a-pagar-e-receber", json=nova_conta)
    assert response.status_code == 201
    assert response.json() == nova_conta_copy


def test_dev_retornar_erro_excedido_descricao():
    response = client.post("/contas-a-pagar-e-receber", json={
        "desc": "Desc teste deve retornar",
        "valor": 12321,
        "tipo": "Pagar"
    })
    
def test_dev_atualizar_conta_a_pagar_e_receber():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    response_put = client.post("/contas-a-pagar-e-receber", json={
        "desc": "Curso de python",
        "valor": 123,
        "tipo": "pagar"
    })

    id_conta_pagar_receber = response_put.json()['id']
    client.put(f"/contas-a-pagar-e-receber/{id_conta_pagar_receber}", json={
        "desc": "Curso de HTML",
        "valor": 111,
        "tipo": "Pagar"
    })
    assert response_put.status_code == 200
    assert response_put.json()['valor'] == 123


def test_dev_remover_conta_a_pagar_e_receber():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    response_put = client.post("/contas-a-pagar-e-receber", json={
        "desc": "Curso de python",
        "valor": 123,
        "tipo": "pagar"
    })

    id_conta_pagar_receber = response_put.json()['id']
    client.delete(f"/contas-a-pagar-e-receber/{id_conta_pagar_receber}")
    assert response_put.status_code == 204