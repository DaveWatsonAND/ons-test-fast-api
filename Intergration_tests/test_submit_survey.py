from fastapi import FastAPI
from fastapi.testclient import TestClient
from api import survey

app = FastAPI()
app.include_router(survey.router)
client = TestClient(app)



def test_submit_survey(mocker):
    mock_return = {
    "fields": {
        "address": "",
        "name": "",
        "city": "",
        "occupation": ""
    },
    "completed": "true",
    "timestamp": "2023-06-12T13:55:45+00:00"
}
    # cloud resourse mock
    mocker.patch("gcp.firestore_client.FireStoreClient.submit_document", return_value=mock_return)
    
    response = client.post("/survey/submit", json={
    "templateId": "test",
    "userId":"test-user"
})


    assert response.status_code == 200
    assert response.json() == mock_return