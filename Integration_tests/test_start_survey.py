from fastapi import FastAPI
from fastapi.testclient import TestClient
from api import survey


app = FastAPI()
app.include_router(survey.router)
client = TestClient(app)



def test_start_survey(mocker):
    mock_return = {
        "firstName": "",
        "lastName": "",
        "age": "",
        "occupation": "",
    }
    # cloud resourse mock
    mocker.patch("gcp.bucket_storage_client.BucketStorageClient.get_json", return_value=mock_return)
    mocker.patch("gcp.firestore_client.FireStoreClient.create_document", return_value=mock_return)
    
    response = client.post("/survey/start", json={
    "templateId": "test",
    "userId":"test-user"
})


    assert response.status_code == 200
    assert response.json() == mock_return