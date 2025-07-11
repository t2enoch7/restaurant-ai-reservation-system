import boto3
from app.models.reservation_model import Reservation, ReservationRequest, ReservationResponse

dynamodb = boto3.resource("dynamodb", endpoint_url="http://dynamodb:8000")
table = dynamodb.Table("Reservations")


# def create_reservation(res: Reservation) -> Reservation:
#     table.put_item(Item=res.dict())
#     return res

def create_reservation(data: ReservationRequest) -> ReservationResponse:
    reservation = Reservation(
        reservation_id=data.reservation_id,
        guest_id=data.guest_id,
        party_size=data.party_size,
        requested_time=data.requested_time,
        status="confirmed",
        table_id=data.table_id,
        preferences=data.preferences
    )

    table.put_item(Item=reservation.model_dump())

    return ReservationResponse(
        reservation_id=reservation.reservation_id,
        status="success"
    )

def get_reservation(reservation_id: str) -> Reservation:
    response = table.get_item(Key={"reservation_id": reservation_id})
    return Reservation(**response["Item"])
