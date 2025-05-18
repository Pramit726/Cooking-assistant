import streamlit as st
from components.comments import comment_section
from recipes import biryani, dosa

st.set_page_config(page_title="Food Blog - Recipes", layout="wide")

st.sidebar.title("🍽️ Recipe Menu")
recipe_option = st.sidebar.selectbox(
    "Choose a Recipe", ["Chicken Biryani", "Dosa", "Add More Recipes"]
)

if recipe_option == "Chicken Biryani":
    biryani.render()
    comment_section("Chicken Biryani")

elif recipe_option == "Dosa":
    dosa.render()
    comment_section("Dosa")

else:
    st.title("🚧 Coming Soon!")
    st.write("More delicious recipes will be added here.")
