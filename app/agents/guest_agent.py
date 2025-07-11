from fastapi import APIRouter
from app.services.guest_service import get_guest_profile, update_guest_profile
from app.models.guest_model import GuestProfile

router = APIRouter()


@router.get("/{guest_id}", response_model=GuestProfile)
def read_guest(guest_id: str):
    return get_guest_profile(guest_id)


@router.post("/", response_model=GuestProfile)
def update_guest(guest: GuestProfile):
    return update_guest_profile(guest)
