from flask import Blueprint, jsonify, request
from src.http_types.http_request import HttpRequest

attendees_route_bp = Blueprint("attendees_route", __name__)

@attendees_route_bp.route("/events/<event_id>/register", methods=["POST"])
def create_attendees(event_id):
    http_request = HttpRequest(param={ "event_id": event_id }, body=request.json)