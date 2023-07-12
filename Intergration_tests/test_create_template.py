from fastapi import FastAPI
from fastapi.testclient import TestClient
from api import template
from main import app
from gcp import BucketStorageClient

app = FastAPI()
app.include_router(template.router)
client = TestClient(app)



def test_create_template(mocker):
    mock_return = {
        "firstName": "",
        "lastName": "",
        "age": "",
        "occupation": "",
    }
    # cloud resourse mock
    mocker.patch("gcp.bucket_storage_client.BucketStorageClient.create_json", return_value=mock_return)
    
    response = client.post("/template/create", json={
    "templateId": "test",
    "data": {
        "firstName": "",
        "lastName": "",
        "age": "",
        "occupation": "",
    }
})


    assert response.status_code == 200
    assert response.json() == mock_return