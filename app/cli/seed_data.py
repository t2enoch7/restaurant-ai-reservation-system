import boto3
import uuid
from datetime import datetime, timedelta

dynamodb = boto3.resource("dynamodb", endpoint_url="http://localhost:8000")


def seed_guests():
    guests = [
        {
            "guest_id": f"g_{i}",
            "name": f"Guest {i}",
            "allergies": [],
            "visits": i,
            "no_shows": 0,
            "favorite_dishes": ["dish_a", "dish_b"]
        } for i in range(10)
    ]
    table = dynamodb.Table("Guests")
    for g in guests:
        table.put_item(Item=g)
    print("✅ Seeded guest profiles.")


def seed_reservations():
    table = dynamodb.Table("Reservations")
    now = datetime.utcnow()
    for i in range(10):
        reservation = {
            "reservation_id": f"res_{i}",
            "guest_id": f"g_{i}",
            "party_size": (i % 4) + 1,
            "requested_time": (now + timedelta(hours=i)).isoformat(),
            "status": "confirmed",
            "table_id": f"T{i % 5}",
            "preferences": []
        }
        table.put_item(Item=reservation)
    print("✅ Seeded reservations.")


if __name__ == "__main__":
    seed_guests()
    seed_reservations()
