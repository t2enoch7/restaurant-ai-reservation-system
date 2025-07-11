from fastapi import APIRouter, HTTPException
from app.services.guest_service import GuestService
from app.models.guest_model import GuestProfile
from typing import List

router = APIRouter()
guest_service = GuestService()


@router.get("/{guest_id}", response_model=GuestProfile)
def get_guest_profile(guest_id: str):
    return guest_service.get_guest_by_id(guest_id)


@router.put("/{guest_id}", response_model=GuestProfile)
def update_guest_profile(guest_id: str, profile: GuestProfile):
    return guest_service.update_guest_profile(guest_id, profile)


@router.post("/{guest_id}/tags", response_model=GuestProfile)
def tag_guest_profile(guest_id: str, tags: List[str]):
    return guest_service.add_tags_to_guest(guest_id, tags)
