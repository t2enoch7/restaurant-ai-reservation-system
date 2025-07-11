from pydantic import BaseModel


class Table(BaseModel):
    table_id: str
    capacity: int
    location: str
    status: str = "available"  # or reserved, cleaning
