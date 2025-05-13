import streamlit as st
import requests

# FastAPI endpoint
API_URL = "http://localhost:8000/chat"

st.set_page_config(page_title="RasoiGuru 🍳", page_icon="🍲")
st.title("🤖 RasoiGuru - Your AI Cooking Assistant")
st.markdown("Ask me anything about cooking, ingredients, or recipes!")

# Chat input
query = st.text_input("👤 You", placeholder="e.g., How to make biryani?")

if query:
    with st.spinner("Cooking up an answer... 🍛"):
        try:
            response = requests.post(API_URL, json={"query": query})
            if response.status_code == 200:
                st.success("RasoiGuru says:")
                st.write(response.json()["response"])
            else:
                st.error(f"Error: {response.status_code} - {response.text}")
        except Exception as e:
            st.error(f"⚠️ Failed to connect to RasoiGuru API\n{e}")