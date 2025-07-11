from fastapi import APIRouter, HTTPException
from app.services.reservation_service import ReservationService
from app.models.reservation_model import ReservationRequest, ReservationResponse, AvailabilityResponse

router = APIRouter()
reservation_service = ReservationService()


@router.post("/check", response_model=AvailabilityResponse)
def check_availability(payload: ReservationRequest):
    return reservation_service.check_availability(payload)


@router.post("/", response_model=ReservationResponse)
def create_reservation(payload: ReservationRequest):
    return reservation_service.create_reservation(payload)
