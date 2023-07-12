from google.cloud import storage
import json
class BucketStorageClient:
    
    def __init__(self):      
     self.client = storage.Client.from_service_account_json("calm-inkwell-392109-71c5cbe50221.json")
     self.bucket = self.client.bucket("template_bucket_example")

    def create_json(self,template_id, data):

        blob = self.bucket.blob(f"{template_id}.json")
        blob.upload_from_string(
        data=json.dumps(data),
        content_type='application/json'
        )
        return self.get_json(template_id)

    def update_json(self,template_id, data):
        # not an ideal solution
        self.delete_json(template_id)  
        return self.create_json(template_id, data)
     
    def get_json(self,file_name):
        blob = self.bucket.blob(f"{file_name}.json")
        file_data = json.loads(blob.download_as_string())
        print(file_data)
        return file_data
    
    def delete_json(self,file_name):
        blob = self.bucket.blob(f"{file_name}.json")
        if(blob.exists()):
            blob.delete()