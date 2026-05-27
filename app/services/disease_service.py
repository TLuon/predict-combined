from sqlalchemy import text

from app.config.database import (
    SessionLocal
)


def get_description(
    disease_name: str
):

    db = SessionLocal()

    try:

        query = text("""

            SELECT description

            FROM diseases

            WHERE disease_name = :name

        """)

        result = db.execute(
            query,
            {
                "name": disease_name
            }
        ).fetchone()

        if result:

            return result[0]

        return "Không có mô tả."

    finally:

        db.close()