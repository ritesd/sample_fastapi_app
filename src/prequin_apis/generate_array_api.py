from fastapi import APIRouter, Depends, Request
from typing import Union
from src.models.api_schema import HTTPError

from src.prequin_apis.api_schema import SentenceInput
from src.prequin_apis.service.array_generator import sentence_to_random_array
from src.user_apis.create_token import JWTBearer

router = APIRouter(prefix="/app")

@router.post(
    path="/generate_array",
    response_model=Union[list, HTTPError], tags=["Prequin API"]
)
async def generate_array(request: Request,input_data: SentenceInput, user: str = Depends(JWTBearer())):
    logger = request.app.logger
    logger.info("API for generating random 500 float array")
    array = sentence_to_random_array(input_data.sentence)
    return array