import boto3
from app.models.guest_model import GuestProfile

dynamodb = boto3.resource("dynamodb", endpoint_url="http://dynamodb:8000")
table = dynamodb.Table("Guests")


def get_guest_profile(guest_id: str) -> GuestProfile:
    response = table.get_item(Key={"guest_id": guest_id})
    return GuestProfile(**response["Item"])


def update_guest_profile(guest: GuestProfile) -> GuestProfile:
    table.put_item(Item=guest.dict())
    return guest
