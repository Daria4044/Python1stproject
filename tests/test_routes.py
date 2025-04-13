from app.main import app

def test_home_route():
    with app.test_client() as client:
        response = client.get("/")
        assert response.status_code == 200
        assert b"KeepFresh" in response.data

def test_404_route():
    with app.test_client() as client:
        response = client.get("/thispagedoesnotexist")
        assert response.status_code == 404
