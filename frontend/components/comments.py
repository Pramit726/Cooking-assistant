import os

import streamlit as st
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv()

# Load DB URL from environment or secrets
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)


def comment_section(recipe_name):
    st.header("💬 Comments")

    with engine.connect() as conn:
        # Fetch existing comments for this recipe
        result = conn.execute(
            text(
                "SELECT name, comment, reply_text, timestamp FROM comments WHERE recipe = :recipe ORDER BY timestamp DESC"
            ),
            {"recipe": recipe_name},
        ).fetchall()

    for row in result:
        name, comment, reply, timestamp = row
        with st.container():
            st.markdown(
                f"**{name}** said at {timestamp.strftime('%Y-%m-%d %H:%M:%S')}"
            )
            st.markdown(f"> {comment}")
            if reply:
                st.success(f"AI Reply: {reply}")
            st.markdown("---")

    # Add new comment
    with st.form(key=f"comment_form_{recipe_name}"):
        st.subheader("Add Your Comment")
        user_name = st.text_input("Your Name")
        user_comment = st.text_area("Your Comment")
        submitted = st.form_submit_button("Submit")

        if submitted and user_name and user_comment:
            with engine.begin() as conn:
                conn.execute(
                    text(
                        """
                        INSERT INTO comments (recipe, name, comment, replied, timestamp)
                        VALUES (:recipe, :name, :comment, FALSE, NOW())
                        """
                    ),
                    {"recipe": recipe_name, "name": user_name, "comment": user_comment},
                )
            st.success("Comment added! Refresh the page to see it below.")
