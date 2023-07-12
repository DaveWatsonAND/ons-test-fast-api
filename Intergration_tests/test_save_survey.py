from fastapi import FastAPI
from fastapi.testclient import TestClient
from api import survey


app = FastAPI()
app.include_router(survey.router)
client = TestClient(app)



def test_save_survey(mocker):
    mock_return = {
        "name": "Chris",
        "age": "",
        "occupation": "",
    }
    # cloud resourse mock
    mocker.patch("gcp.firestore_client.FireStoreClient.update_document", return_value=mock_return)
    
    response = client.post("/survey/save", json={
    "templateId": "test",
    "userId":"test-user",
    "data": {
        "name": "Chris"
    }
})


    assert response.status_code == 200
    assert response.json() == mock_return