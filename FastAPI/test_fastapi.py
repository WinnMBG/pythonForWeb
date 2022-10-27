from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_route():
	response = client.get("/")
	assert response.status_code == 200
	assert response.json() == {"message" :"hello world!"}
	
def test_ids():
	response = client.get("/ids/2")
	assert response.status_code == 200
	assert response.json() == {"identifiant" : 2}

