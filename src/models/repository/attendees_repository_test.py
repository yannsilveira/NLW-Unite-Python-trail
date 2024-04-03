from .attendees_repository import AttendeesRepository
from src.models.settings.connection import db_connection_handler
import pytest

db_connection_handler.connect_to_db()

@pytest.mark.skip(reason="Criara um novo registro no banco")
def test_insert_attendee():
    event_id = "meu-uuid"
    attendees_info = {
        "uuid": "uuid_attendee",
        "name": "attendee name",
        "email": "attendee@gmail.com",
        "event_id": event_id
    }
    attendees_repository = AttendeesRepository()
    response = attendees_repository.insert_attendee(attendees_info)
    print(response)

def test_get_attendee_by_id():
    attendee_id = "uuid_attendee"
    attendee_repository = AttendeesRepository()
    attendee = attendee_repository.get_attendee_badge_by_id(attendee_id)

    print(attendee)
