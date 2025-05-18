import streamlit as st


def render():
    st.title("🥞 Dosa Recipe with Batter")
    st.subheader("Crispy South Indian lentil crepes (Dosa)")
    st.markdown(
        "Made from fermented batter of rice and urad dal. Serve with chutney and sambar."
    )
    st.info(
        "⏰ **Total Time**: 12 hrs 25 mins | 🥄 **Makes**: 12 dosas | ✍️ **Author**: Swasthi"
    )

    st.header("🥘 Ingredients")
    st.subheader("• Batter")
    st.markdown(
        """
- Urad dal, chana dal, fenugreek  
- Rice, poha, salt  
- Water to blend
"""
    )

    st.header("👨‍🍳 Instructions")
    st.markdown(
        """
1. Soak ingredients separately  
2. Blend and ferment  
3. Spread on hot tawa  
4. Cook until crisp and golden
"""
    )

    st.header("📊 Nutrition Info")
    st.markdown("Calories: 123 | Protein: 4g | Carbs: 25g | Iron: 1.7mg")

    st.caption(
        "Source: [Swasthi’s Dosa](https://www.indianhealthyrecipes.com/dosa-recipe-dosa-batter/)"
    )
