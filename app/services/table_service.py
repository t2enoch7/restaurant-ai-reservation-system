import boto3
from app.models.table_model import Table

dynamodb = boto3.resource("dynamodb", endpoint_url="http://dynamodb:8000")
table = dynamodb.Table("Tables")


def get_table(table_id: str) -> Table:
    response = table.get_item(Key={"table_id": table_id})
    return Table(**response["Item"])


def update_table_status(table_id: str, status: str) -> Table:
    table.update_item(
        Key={"table_id": table_id},
        UpdateExpression="SET #s = :status",
        ExpressionAttributeNames={"#s": "status"},
        ExpressionAttributeValues={":status": status}
    )
    return get_table(table_id)
