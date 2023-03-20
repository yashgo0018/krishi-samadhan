from pydantic import BaseModel


class SuggestCropBody(BaseModel):
    N: float
    P: float
    K: float
    temperature: float
    humidity: float
    ph: float
    rainfall: float
