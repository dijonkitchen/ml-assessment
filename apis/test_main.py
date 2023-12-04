from fastapi.testclient import TestClient

from apis.main import PredRequest, app

client = TestClient(app)


def test_predict():
    request = PredRequest(message="test message")

    subject = client.post("/predict", json=request.model_dump())

    assert subject.status_code == 200

    assert "status" in subject.json()
    assert "prediction" in subject.json()

    for pred in subject.json()["prediction"]:
        assert "label" in pred
        assert "weight" in pred
