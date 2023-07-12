from fastapi import FastAPI
from fastapi.testclient import TestClient
from api import template
from main import app


app = FastAPI()
app.include_router(template.router)
client = TestClient(app)


def test_update_template(mocker):
    mock_return = {
        "firstName": "",
        "lastName": "",
    }
    mocker.patch("gcp.bucket_storage_client.BucketStorageClient.update_json", return_value=mock_return)
    
    response = client.post("/template/update", json={
    "templateId": "test",
    "data": {
        "firstName": "",
        "lastName": "",
    }
})

    assert response.status_code == 200
    assert response.json() == mock_return