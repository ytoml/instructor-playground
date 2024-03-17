from typing import Literal, Type, TypeVar

from instructor import patch
from openai import OpenAI
from openai.types.chat import ChatCompletionMessageParam
from pydantic import BaseModel

__DUMMY_API_KEY = "dummy"
DUMMY_OPENAI_MODEL = "gpt-3.5-turbo"

BASE_URL = "http://0.0.0.0:8000"

T = TypeVar("T")


client = patch(OpenAI(api_key=__DUMMY_API_KEY, base_url=BASE_URL))


class Params(BaseModel):
    max_tokens: int
    temperature: float | None
    top_p: float | None


def extract_model(
    messages: list[ChatCompletionMessageParam],
    params: Params,
    response_model: Type[T],
) -> T:
    response = client.chat.completions.create(
        messages=messages,
        model=DUMMY_OPENAI_MODEL,
        response_model=response_model,
        **params.model_dump()
    )
    return response
