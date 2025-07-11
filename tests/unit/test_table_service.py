import pytest
from app.services.table_service import TableService


@pytest.fixture
def dummy_table_data():
    return [
        {"table_id": "T1", "seats": 2, "status": "available"},
        {"table_id": "T2", "seats": 4, "status": "available"},
        {"table_id": "T3", "seats": 6, "status": "occupied"}
    ]


def test_find_best_fit_table(dummy_table_data):
    service = TableService(table_data=dummy_table_data)
    table = service.find_table(party_size=4)
    assert table is not None
    assert table["table_id"] == "T2"


def test_no_available_table(dummy_table_data):
    service = TableService(table_data=dummy_table_data)
    table = service.find_table(party_size=10)
    assert table is None
