from fastapi import APIRouter
from app.services.reservation_service import create_reservation, get_reservation
from app.models.reservation_model import Reservation

router = APIRouter()


@router.post("/", response_model=Reservation)
def create(res: Reservation):
    return create_reservation(res)


@router.get("/{reservation_id}", response_model=Reservation)
def read(reservation_id: str):
    return get_reservation(reservation_id)
