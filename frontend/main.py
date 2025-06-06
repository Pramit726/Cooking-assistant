import streamlit as st
from components.comments import comment_section
from recipes.breakfast import masaladosa, upma
from recipes.dessert import kheer
from recipes.non_veg_curry import chicken_bhuna_masala, chicken_butter_masala
from recipes.rice_non_veg import chicken_biryani
from recipes.rice_veg import pulao
from recipes.snacks import onion_bhaji, samosa
from recipes.veg_curry import aloo_gobi, baingan_bharta
from recipes.dessert import gulab_jamun, kheer

st.set_page_config(page_title="Food Blog - Recipes", layout="wide")

st.sidebar.title("🍽️ Recipe Menu")

# Add a category selection
category_option = st.sidebar.selectbox(
    "Choose a Category",
    [
        "Breakfast",
        "Snacks",
        "Rice(Veg)",
        "Rice(Non-veg)",
        "Curry(Veg)",
        "Curry(Non-veg)",
        "Dessert",
        "Other Categories (Coming Soon)",
    ],
)

if category_option == "Breakfast":
    st.sidebar.subheader("Breakfast")
    recipe_option = st.sidebar.selectbox(
        "Select a Breakfast Recipe", ["Upma", "Masala Dosa"]
    )

    if recipe_option == "Upma":
        upma.render()
        comment_section("upma")

    elif recipe_option == "Masala Dosa":
        masaladosa.render()
        comment_section("masaladosa")


if category_option == "Snacks":
    st.sidebar.subheader("Snacks")
    recipe_option = st.sidebar.selectbox(
        "Select a Snack Recipe", ["Onion Bhaji", "Samosa"]
    )

    if recipe_option == "Onion Bhaji":
        onion_bhaji.render()
        comment_section("onionbhaji")

    elif recipe_option == "Samosa":
        samosa.render()
        comment_section("samosa")


if category_option == "Rice(Veg)":
    st.sidebar.subheader("Rice(Veg)")
    recipe_option = st.sidebar.selectbox("Select a Rice(Veg) Recipe", ["Pulao"])

    if recipe_option == "Pulao":
        pulao.render()
        comment_section("pulao")


if category_option == "Rice(Non-veg)":
    st.sidebar.subheader("Rice(Non-veg)")
    recipe_option = st.sidebar.selectbox(
        "Select a Rice(Non-veg) Recipe", ["Chicken Biryani"]
    )

    if recipe_option == "Chicken Biryani":
        chicken_biryani.render()
        comment_section("chickenbiryani")


if category_option == "Curry(Veg)":
    st.sidebar.subheader("Curry(Veg)")
    recipe_option = st.sidebar.selectbox(
        "Select a Curry(Veg) Recipe", ["Aloo Gobi", "Baingan Bharta"]
    )

    if recipe_option == "Aloo Gobi":
        aloo_gobi.render()
        comment_section("aloogobi")

    elif recipe_option == "Baingan Bharta":
        baingan_bharta.render()
        comment_section("bainganbharta")

if category_option == "Curry(Non-veg)":
    st.sidebar.subheader("Curry(Non-veg)")
    recipe_option = st.sidebar.selectbox(
        "Select a Curry(Non-veg) Recipe",
        ["Chicken Bhuna Masala", "Chicken Butter Masala"],
    )

    if recipe_option == "Chicken Bhuna Masala":
        chicken_bhuna_masala.render()
        comment_section("chickenbhunamasala")

    elif recipe_option == "Chicken Butter Masala":
        chicken_butter_masala.render()
        comment_section("chickenbuttermasala")


if category_option == "Dessert":
    st.sidebar.subheader("Dessert")
    recipe_option = st.sidebar.selectbox(
        "Select a Dessert Recipe", ["Gulab Jamun", "Kheer"]
    )

    if recipe_option == "Gulab Jamun":
        gulab_jamun.render()
        comment_section("gulabjamun")

    elif recipe_option == "Kheer":
        kheer.render()
        comment_section("kheer")


elif category_option == "Other Categories (Coming Soon)":
    st.title("🚧 Coming Soon!")
    st.write("More delicious recipes and categories will be added here.")
