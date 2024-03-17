from pydantic import BaseModel
import IPython

from mylib.model import Params, extract_model


class UserDetail(BaseModel):
    name: str
    age: int


response = extract_model(
    messages=[{"role": "user", "content": "Extract Jason is 25 years old"}],
    params=Params(max_tokens=100, temperature=0.7, top_p=1),
    response_model=UserDetail,
)

assert isinstance(response, UserDetail)
assert response.name == "Jason"
assert response.age == 25

IPython.embed()
