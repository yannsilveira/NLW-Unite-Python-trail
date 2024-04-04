from flask import Blueprint, jsonify, request
from src.http_types.http_request import HttpRequest
from src.data.check_in_handler import CheckInHandler
from src.errors.error_handler import handle_error

check_in_route_bp = Blueprint("check_in_route", __name__)

@check_in_route_bp.route("/check-in/register", methods=["POST"])
def create_attendees():
    try:
        check_in_handler = CheckInHandler()
        http_request = HttpRequest(body=request.json)

        http_response = check_in_handler.register_check_in(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_error(exception)
        return jsonify(http_response.body), http_response.status_code

