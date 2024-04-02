from src.models.settings.connection import db_connection_handler
from .events_repository import EventsRepository
import pytest

db_connection_handler.connect_to_db()

@pytest.mark.skip(reason="Criara um novo registro no banco")
def test_insert_event():
    event = {
        "uuid": "meu-uuid2",
        "title": "Title",
        "slug": "Slug2",
        "maximum_attendees": 20 
    }

    events_repository = EventsRepository()
    response = events_repository.insert_event(event)
    print(response)

@pytest.mark.skip(reason="Recupera algo sem necessidade no momento")
def test_get_event_by_id():
    event_id = "meu-uuid2"
    event_repository = EventsRepository()
    response = event_repository.get_event_by_id(event_id)
    print(response)