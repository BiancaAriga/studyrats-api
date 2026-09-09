from fastapi import APIRouter

from app.services.quotes import get_random_quote
from app.schemas.quote import QuoteResponse

router = APIRouter(
    prefix="/quotes",
    tags=["Quotes"],
)


@router.get(
    "/random",
    response_model=QuoteResponse,
)
def random_quote():
    return get_random_quote()