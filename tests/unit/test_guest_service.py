from app.models.guest_model import GuestProfile
from app.services.guest_service import create_guest, get_guest


def test_guest_create_and_fetch(monkeypatch):
    dummy_guest = GuestProfile(
        guest_id="test_g_1",
        name="Test Guest",
        allergies=["shellfish"],
        visits=3,
        no_shows=0,
        favorite_dishes=["pasta"]
    )
    monkeypatch.setenv("AWS_ACCESS_KEY_ID", "test")
    monkeypatch.setenv("AWS_SECRET_ACCESS_KEY", "test")

    created = create_guest(dummy_guest)
    fetched = get_guest("test_g_1")
    assert fetched.name == "Test Guest"
    assert "pasta" in fetched.favorite_dishes
