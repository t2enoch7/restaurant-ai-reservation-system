import boto3
from dotenv import load_dotenv
import os

load_dotenv()

dynamodb = boto3.resource(
    'dynamodb',
    region_name=os.getenv("AWS_REGION"),
    endpoint_url=os.getenv("DYNAMODB_ENDPOINT")
)


def create_reservations_table():
    try:
        table = dynamodb.create_table(
            TableName='Reservations',
            KeySchema=[
                {'AttributeName': 'reservation_id', 'KeyType': 'HASH'}
            ],
            AttributeDefinitions=[
                {'AttributeName': 'reservation_id', 'AttributeType': 'S'}
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 5, 'WriteCapacityUnits': 5}
        )
        table.wait_until_exists()
        print("✅ Reservations table created.")
    except Exception as e:
        print("⚠️ Table may already exist:", e)


def seed_fake_reservations():
    table = dynamodb.Table('Reservations')
    for i in range(10):
        table.put_item(Item={
            "reservation_id": f"res_{i}",
            "guest_id": f"g_{i}",
            "party_size": (i % 4) + 2,
            "requested_time": "2025-07-09T18:30:00Z",
            "status": "confirmed",
            "table_id": f"T{i}",
            "preferences": ["window"] if i % 2 == 0 else ["quiet"]
        })
    print("✅ Seeded 10 fake reservations.")

def create_guest_profiles_table():
    try:
        table = dynamodb.create_table(
            TableName='GuestProfiles',
            KeySchema=[{'AttributeName': 'guest_id', 'KeyType': 'HASH'}],
            AttributeDefinitions=[
                {'AttributeName': 'guest_id', 'AttributeType': 'S'}],
            ProvisionedThroughput={
                'ReadCapacityUnits': 5, 'WriteCapacityUnits': 5}
        )
        table.wait_until_exists()
        print("✅ GuestProfiles table created.")
    except Exception as e:
        print("⚠️ Table may already exist:", e)


def seed_fake_guests():
    table = dynamodb.Table('GuestProfiles')
    for i in range(10):
        table.put_item(Item={
            "guest_id": f"g_{i}",
            "name": f"Guest {i}",
            "allergies": ["nuts"] if i % 2 == 0 else [],
            "visits": i,
            "no_shows": i % 3,
            "favorite_dishes": ["pasta", "salmon"]
        })
    print("✅ Seeded 10 fake guest profiles.")



if __name__ == "__main__":
    create_reservations_table()
    seed_fake_reservations()
    create_guest_profiles_table()
    seed_fake_guests()
