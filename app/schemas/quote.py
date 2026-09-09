from pydantic import BaseModel


class QuoteResponse(BaseModel):
    quote: str
    author: str