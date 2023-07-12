from abstract import IRepository
from gcp import BucketStorageClient


class TemplateRepository(IRepository):
    def __init__(self):
        self.client = BucketStorageClient()
        return

    def update(self, template_id, data):
        return self.client.update_json(template_id, data)

    def create(self,template_id, data):
        return self.client.create_json(template_id ,data)
    
    def get(self, template_id):
        return self.client.get_json(template_id)
