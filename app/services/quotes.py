import requests

from app.schemas.quote import QuoteResponse

def get_random_quote() -> QuoteResponse:
    response = requests.get(
        "https://zenquotes.io/api/random"
    )

    response.raise_for_status()

    data = response.json()[0]

    return QuoteResponse(
        quote=data["q"],
        author=data["a"],
    )