from pydantic import BaseModel
from typing import List


class GuestProfile(BaseModel):
    guest_id: str
    name: str
    allergies: List[str]
    visits: int = 0
    no_shows: int = 0
    favorite_dishes: List[str] = []
