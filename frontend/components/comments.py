from datetime import datetime

import streamlit as st
from db_config import engine
from sqlalchemy.sql import text


def comment_section(recipe_key):
    st.markdown("---")
    st.subheader("💬 Leave a Comment")

    with st.form(f"form_{recipe_key}"):
        name = st.text_input("Name", key=f"name_{recipe_key}")
        comment_text = st.text_area("Comment", key=f"comment_{recipe_key}")
        if st.form_submit_button("Submit Comment") and name and comment_text:
            with engine.begin() as conn:
                conn.execute(
                    text(
                        """
                    INSERT INTO comments (recipe, name, comment)
                    VALUES (:recipe, :name, :comment)
                """
                    ),
                    {"recipe": recipe_key, "name": name, "comment": comment_text},
                )
            st.success("Thanks for your comment!")

    with engine.connect() as conn:
        results = conn.execute(
            text(
                """
            SELECT name, comment, timestamp FROM comments
            WHERE recipe = :recipe ORDER BY timestamp DESC
        """
            ),
            {"recipe": recipe_key},
        ).fetchall()

    if results:
        st.markdown("### 📝 Comments")
        for name, comment, timestamp in results:
            st.markdown(
                f"**{name}** wrote on _{timestamp.strftime('%Y-%m-%d %H:%M:%S')}_:"
            )
            st.markdown(f"> {comment}")
            st.markdown("---")
