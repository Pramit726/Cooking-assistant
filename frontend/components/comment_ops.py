from db_config import engine
from sqlalchemy.sql import text


def fetch_unreplied_comments():
    with engine.connect() as conn:
        return conn.execute(
            text(
                """
            SELECT id, recipe, name, comment FROM comments
            WHERE replied = FALSE AND timestamp < NOW() - INTERVAL '24 hours'
        """
            )
        ).fetchall()


def update_comment_reply(comment_id: int, reply: str):
    with engine.begin() as conn:
        conn.execute(
            text(
                """
            UPDATE comments
            SET replied = TRUE, reply_text = :reply
            WHERE id = :id
        """
            ),
            {"id": comment_id, "reply": reply},
        )
