from abstract import IRepository
from gcp import FireStoreClient


class SurveyRepository(IRepository):
    def __init__(self):
        self.client = FireStoreClient()
        return

    def update(self, document, userId, templateId):
        return self.client.update_document(document, userId, templateId)

    def create(self, document, userId, templateId):
        return self.client.create_document(document, userId, templateId)

    def submit(self, document, userId, templateId):
        return self.client.submit_document(document, userId, templateId)
