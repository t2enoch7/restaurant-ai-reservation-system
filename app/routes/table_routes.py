from fastapi import APIRouter
from app.services.table_service import TableService
from app.models.table_model import TableStatusUpdate, TableStatusResponse

router = APIRouter()
table_service = TableService()


@router.post("/{table_id}/status", response_model=TableStatusResponse)
def update_table_status(table_id: str, payload: TableStatusUpdate):
    return table_service.update_table_status(table_id, payload.status)
