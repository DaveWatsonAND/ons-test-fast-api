from repository import SurveyRepository
from repository import TemplateRepository
import calendar
import time
from datetime import datetime

current_GMT = time.gmtime()

time_stamp = calendar.timegm(current_GMT)
date_time = datetime.fromtimestamp(time_stamp)


class SurveyService:
    def __init__(self):
        self.repository = SurveyRepository()
        self.template_repository = TemplateRepository()

    def start_survey(self, template_id, user_id):
        template = self.template_repository.get(template_id)
        return self.repository.create(template, user_id, template_id)

    def save_survey(self, form_data, user_id, template_id):
        return self.repository.update(form_data, user_id, template_id)

    def submit_survey(self, user_id, template_id):
        form_data = dict({"completed": "true", "timestamp": date_time})
        return self.repository.submit(form_data, user_id, template_id)

