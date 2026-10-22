from app import app


def test_home():
    with app.test_client() as client:
        response = client.get("/")
        assert response.status_code == 200
        assert response.get_data(as_text=True) == "CI/CD demo version 1"


def test_health():
    with app.test_client() as client:
        response = client.get("/health")
        assert response.status_code == 200
        assert response.get_json() == {"status": "ok"}
