from repository import TemplateRepository

class TemplateService:
    def __init__(self):
        self.repsitory = TemplateRepository()


    def create_template(self,template_id, data):
        return self.repsitory.create(template_id, data)
        
    
    def update_template(self,template_id, data):
         return self.repsitory.update(template_id, data)
     
     
    def fetch_template(self, template_id):
        return self.repsitory.get(template_id)
        