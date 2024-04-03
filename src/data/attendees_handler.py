import uuid
from src.models.repository.attendees_repository import AttendeesRepository
from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse
from src.models.repository.events_repository import EventsRepository

class AttendeesHandler:
    def __init__(self) -> None:
        self.__attendees_repository = AttendeesRepository()
        self.__events_repository = EventsRepository()

    def registry(self, http_request: HttpRequest) -> HttpResponse:
        body = http_request.body
        event_id = http_request.param["event_id"]

        events_attendees_count = self.__events_repository.count_event_attendees(event_id)
        if (events_attendees_count["attendeesAmount"] 
            and events_attendees_count["maxAttendees"] < events_attendees_count["attendeesAmount"]):
            raise Exception("Evento já preencheu todas as vagas!")
        
        body["uuid"] = str(uuid.uuid4())
        body["event_id"] = event_id
        self.__attendees_repository.insert_attendee(body)

        return HttpResponse(body = None, status_code = 201)


