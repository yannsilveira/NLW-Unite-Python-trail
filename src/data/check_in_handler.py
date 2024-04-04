from src.models.repository.check_ins_repository import CheckInRepository
from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse

class CheckInHandler:
    def __init__(self) -> None:
        self.__check_in_repository = CheckInRepository()

    def register_check_in(self, http_request: HttpRequest) -> HttpResponse:
        check_in_infos = http_request.body["attendeeId"]
        http_response = self.__check_in_repository.insert_check_in(check_in_infos)

        return HttpResponse(
            body = None,
            status_code = 201
        )
