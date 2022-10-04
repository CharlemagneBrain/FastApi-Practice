from fastapi.testclient import TestClient

def test_acceuil(client: TestClient):
    
    response = client.get("/")
    assert response.status_code == 200 # asser=> permet de nous assurer que la condition qui suit est vraie (verifier le code status 200)
    assert "Actuel url" in response.text # On test mm le contenu renvoyé




