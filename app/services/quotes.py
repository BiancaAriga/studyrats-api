import random

import requests
from fastapi import HTTPException, status

from app.cache.quote_cache import quote_cache
from app.schemas.quote import QuoteResponse


def load_quotes():
    try:
        response = requests.get(
            "https://zenquotes.io/api/quotes"
        )

        response.raise_for_status()

        data = response.json()

    except requests.RequestException:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Não foi possível obter as frases no momento.",
        )

    quote_cache.quotes = [
        QuoteResponse(
            quote=quote["q"],
            author=quote["a"],
        )
        for quote in data
    ]


def get_random_quote() -> QuoteResponse:
    if quote_cache.is_empty():
        load_quotes()

    return random.choice(quote_cache.quotes)