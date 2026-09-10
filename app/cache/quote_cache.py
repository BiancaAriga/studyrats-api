from app.schemas.quote import QuoteResponse


class QuoteCache:
    def __init__(self):
        self.quotes: list[QuoteResponse] = []

    def is_empty(self) -> bool:
        return not self.quotes
    
quote_cache = QuoteCache()