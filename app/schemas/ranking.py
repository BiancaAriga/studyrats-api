from pydantic import BaseModel


class RankingResponse(BaseModel):
    user_id: int
    user_name: str
    total_duration: int