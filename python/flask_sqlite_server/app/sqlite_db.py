"""The database module of the http server."""

import json
import pathlib
import sqlite3

DATABASE_PATH = (
    pathlib.Path(__file__).resolve().parent / "database" / "sqlite_data.db"
)


def init_database() -> None:
  """Initializes the database."""

  # Makes sure the database directory exists.
  DATABASE_PATH.parent.mkdir(parents=True, exist_ok=True)

  # Creates the database if it doesn't exist.
  with sqlite3.connect(DATABASE_PATH) as conn:
    conn.execute("""
            CREATE TABLE IF NOT EXISTS payloads (
                id   INTEGER PRIMARY KEY AUTOINCREMENT,
                data TEXT NOT NULL
            )
            """)


def save_payload(payload: dict[str, str]) -> int:
  """Saves the payload to the database.

  Args:
    payload: The payload to be saved.

  Returns:
    The id of the saved payload.
  """

  # Inserts the payload into the database.
  with sqlite3.connect(DATABASE_PATH) as conn:
    cursor = conn.execute(
        """
        INSERT INTO payloads (data) VALUES (?)
        """,
        (json.dumps(payload),),
    )
    conn.commit()
    return cursor.lastrowid
