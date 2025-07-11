from pydantic import BaseModel, Field
from typing import List, Optional


class Reservation(BaseModel):
    reservation_id: str
    guest_id: str
    party_size: int
    requested_time: str  # ISO 8601
    status: str = "pending"
    table_id: str = None
    preferences: List[str] = []


class ReservationRequest(BaseModel):
    guest_id: str
    party_size: int
    requested_time: str  # ISO 8601
    preferences: Optional[List[str]] = Field(default_factory=list)


class ReservationResponse(BaseModel):
    reservation_id: str
    status: str
    table_id: Optional[str] = None
    message: Optional[str] = None
