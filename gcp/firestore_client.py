import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate(
    "calm-inkwell-392109-firebase-adminsdk-nfgza-568e25399a.json"
)


class FireStoreClient:
    def __init__(self):
        app = firebase_admin.initialize_app(cred)
        self.firestore_client = firestore.client()

    def create_document(self, document, user_id, template_id):
        doc_ref = self.firestore_client.collection("surveys").document(user_id)
        form_ref = doc_ref.collection(template_id).document("data")
        form_ref.set({"fields": document})
        return self.get_document(user_id, template_id)

    def update_document(self, document, user_id, template_id):
        doc_ref = self.firestore_client.collection("surveys").document(user_id)
        form_ref = doc_ref.collection(template_id).document("data")
        form_ref.update({"fields": document})
        return self.get_document(user_id, template_id)

    def submit_document(self, document, user_id, template_id):
        doc_ref = self.firestore_client.collection("surveys").document(user_id)
        form_ref = doc_ref.collection(template_id).document("data")
        form_ref.update(document)
        return self.get_document(user_id, template_id)

    def get_document(self, user_id, template_id):
        doc_ref = self.firestore_client.collection("surveys").document(user_id)
        form_ref = doc_ref.collection(template_id).document("data")
        data = form_ref.get()
        return data.to_dict()
