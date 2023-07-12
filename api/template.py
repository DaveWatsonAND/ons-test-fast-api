from fastapi import APIRouter
from service import TemplateService
from pydantic import BaseModel
from typing import Any


router = APIRouter()

template_service = TemplateService()


class TemplateBody(BaseModel):
    templateId: str
    data: Any



@router.post("/template/create", tags=["survey"])
async def create_template(body:TemplateBody):
    print(body)
    request_dict = dict(body)
    template_id = request_dict.get("templateId")
    form_data = request_dict.get("data")
    data = template_service.create_template(template_id, form_data)
    return data


@router.post("/template/update", tags=["survey"])
async def update_template(body:TemplateBody):
    request_dict = dict(body)
    template_id = request_dict.get("templateId")
    form_data = request_dict.get("data")
    data = template_service.update_template(template_id, form_data)
    return data
