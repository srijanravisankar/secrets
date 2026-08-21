from pydantic import BaseModel


class GifSearchResponse(BaseModel):
    urls: list[str]
