"""Flask route definitions."""

from typing import Any, Dict
from flask import Blueprint, abort, current_app, jsonify, request
from . import db
from .models import Payload

api_bp = Blueprint("api", __name__)


@api_bp.route("/data", methods=["POST"])
def add_payload():
  """Add a payload to the database.

  The function will:
  1. Check if the request is in json format.
  2. Get the payload from the request.
  3. Save the payload to the database.
  4. Return the status of the request and the id of the payload.

  Returns:
      JSON response with status and message.
  """
  current_app.logger.info("Received POST request for /data")

  if not request.json:
    current_app.logger.warning("Request Content-Type is not application/json")
    abort(400, "Context-Type should be application/json")

  payload: Dict[str, Any] = request.get_json(force=True)

  current_app.logger.debug(f"Received payload: {payload}")

  try:
    row = Payload(data=payload)
    current_app.logger.info("Adding payload to database session...")
    db.session.add(row)
    db.session.commit()
    current_app.logger.info(f"Payload saved successfully with id: {row.id}")

    return jsonify(
        status=200,
        message="Payload saved successfully.",
        row_id=row.id,
    )
  except Exception as e:
    db.session.rollback()
    current_app.logger.error(f"Failed to save payload: {e}", exc_info=True)
    abort(500, description=f"Failed to save payload: {e}")
