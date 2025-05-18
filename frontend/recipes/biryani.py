import streamlit as st


def render():
    st.title("🍗 Chicken Biryani Recipe")
    st.subheader("Aromatic, delicious and spicy one-pot chicken biryani")
    st.markdown(
        """
Made with basmati rice, spices, chicken and herbs.  
This is a beginner-friendly recipe and can be made with ease.  
**Serve it with raita or salan (gravy).**
"""
    )
    st.info(
        "⏰ **Total Time**: 1 hr 25 mins | 👨‍🍳 **Serves**: 4 people | ✍️ **Author**: Swasthi"
    )

    st.header("🥘 Ingredients")
    st.subheader("• Marinade")
    st.markdown(
        """
- ½ kg chicken  
- 3 tbsp yogurt  
- 1¼ tbsp ginger garlic paste  
- ½ to ¾ tsp salt  
- ¼ tsp turmeric  
- ½ to 1 tsp red chilli powder  
- ½ to 1 tbsp garam masala  
- 1 tbsp lemon juice (optional)
"""
    )
    st.subheader("• Whole Spices")
    st.markdown("Bay leaf, cardamom, cloves, cinnamon, star anise, shahi jeera, mace")

    st.subheader("• Others")
    st.markdown(
        "Rice, ghee/oil, onions, mint, chili, yogurt, water, salt, fried onions, saffron"
    )

    st.header("👨‍🍳 Instructions")
    st.markdown(
        "1. Marinate chicken and soak rice.\n2. Cook chicken with spices.\n3. Layer rice.\n4. Cook and serve."
    )

    st.header("📊 Nutrition Info")
    st.markdown("Calories: 753 | Protein: 34g | Carbs: 86g | Fat: 29g")

    st.caption(
        "Source: [Swasthi’s Chicken Biryani](https://www.indianhealthyrecipes.com/chicken-biryani-recipe/)"
    )
