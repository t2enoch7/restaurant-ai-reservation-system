from fastapi import APIRouter
from app.services.table_service import get_table, update_table_status

router = APIRouter()


@router.get("/{table_id}")
def fetch(table_id: str):
    return get_table(table_id)


@router.post("/{table_id}/status")
def update_status(table_id: str, status: str):
    return update_table_status(table_id, status)
