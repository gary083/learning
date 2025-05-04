"""The flask server."""

from typing import Any, Dict
from flask import Flask, abort, jsonify, request
from sqlite_db import init_database, save_payload


app = Flask(__name__)
init_database()


@app.route('/data', methods=['POST'])
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
  # Checks the request is in json format.
  if not request.json:
    app.logger.error('Context-Type should be application/json')
    abort(400, 'Context-Type should be application/json')

  payload: Dict[str, Any] = request.get_json(force=True)

  try:
    row_id = save_payload(payload)
    app.logger.info(
        f'Payload saved successfully. Row id: {row_id}. Payload: {payload}'
    )
    return jsonify(
        status=200,
        message='Payload saved successfully.',
        row_id=row_id,
    )
  except Exception as e:
    app.logger.error(f'Failed to save payload: {e}')
    abort(500, description=f'Failed to save payload: {e}')


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=True)
