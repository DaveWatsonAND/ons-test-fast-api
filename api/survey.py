from fastapi import APIRouter
from service import SurveyService
from pydantic import BaseModel
from typing import Any


router = APIRouter()

service = SurveyService()



class SurveyBody(BaseModel):
    userId: str
    templateId: str


class SaveSurveyBody(SurveyBody):
    data: Any


@router.post("/survey/start", tags=["survey"])
async def start_survey(body: SurveyBody):
    request_dict = dict(body)
    user_id = request_dict.get("userId")
    template_id = request_dict.get("templateId")

    data = service.start_survey(
        template_id,
        user_id,
    )
    return data


@router.post("/survey/save", tags=["survey"])
async def save_survey(body: SaveSurveyBody):
    request_dict = dict(body)
    user_id = request_dict.get("userId")
    form_data = request_dict.get("data")
    template_id = request_dict.get("templateId")
    data = service.save_survey(form_data, user_id, template_id)
    return data


@router.post("/survey/submit", tags=["survey"])
async def submit_survey(body: SurveyBody):
    request_dict = dict(body)
    user_id = request_dict.get("userId")
    template_id = request_dict.get("templateId")
    data = service.submit_survey(user_id, template_id)
    return data
