import streamlit as st


def render():
    st.title("🧅 Onion Bhaji Recipe")
    st.subheader("Crispy and flavorful deep-fried onion fritters")
    st.markdown(
        """
A popular Indian snack, perfect with chutney or as a side dish.
"""
    )
    # The original page doesn't have explicit prep/cook times displayed prominently like the biryani
    # We can estimate or omit if not available from the source.
    # Based on general knowledge, it's a quick recipe. Let's make a reasonable estimate.
    st.info(
        "⏰ **Total Time**: Approx. 40 mins | 👨‍🍳 **Serves**: Varies | ✍️ **Author**: Swasthi"
    )

    st.header("🥘 Ingredients")
    st.markdown(
        """
- 200 grams (2 cups, 1 medium) onion sliced (yellow/brown or red)
- 1 green chili (fine chopped, optional)
- 1 tablespoon ginger (minced/grated or use 1 tablespoon ginger garlic paste)
- 1 tablespoon garlic (minced/grated, omit if using ginger garlic paste)
- ¼ cup coriander leaves (fine chopped)
- ¾ cup (85 grams) besan (gram flour)
- ⅓ cup (45 grams) rice flour (or use ¼ cup corn starch)
- ½ to ¾ teaspoon sea salt (adjust to taste)
- ⅛ teaspoon baking soda (optional)
- ½ teaspoon red chili powder or flakes
- 1 teaspoon coriander powder
- ½ teaspoon carom seeds / ajwain/ fennel seeds
- ¾ teaspoon garam masala
- 1 to 3 tablespoons water (use only as required)
- High smoke point oil to deep fry – about 1½ cups
"""
    )

    st.header("👨‍🍳 Instructions")
    st.markdown(
        """
1.  **Prepare Onions:** Slice onions thin and add to a large mixing bowl. Add salt and mix well, squeezing gently to release juices. Rest for 15 to 20 mins.
2.  **Heat Oil:** On a medium flame, heat oil in a deep pan for deep frying.
3.  **Make Batter:** Meanwhile, add all ingredients except water to the onions and mix well with your hand. If the batter is too dry, sprinkle 1 tablespoon of water and mix.
4.  **Test Oil:** Drop a small portion of batter into the hot oil. It should sizzle and rise to the surface without browning.
5.  **Fry Bhajis (First Fry):** Take ¾ tablespoon portions of batter with your fingers and slide them into the hot oil. Do not shape them. Avoid overcrowding and do not touch them for 2 to 3 mins. Fry on medium heat for 3 mins, stirring occasionally until crisp and light golden. Remove to a cooling rack. Fry in batches.
6.  **Refry (Optional for Extra Crispness):** Refry for 1 to 2 mins for an extra crisp texture.
7.  **Serve:** Onion bhajis are best served hot, immediately as they begin to lose their crispness when they sit.
"""
    )

    # Nutrition info is available on the source page's recipe card.
    # I've included the most common ones.
    st.header("📊 Nutrition Info (Approximate per serving)")
    st.markdown("Calories: 263kcal | Carbohydrates: 27g | Protein: 7g | Fat: 14g")

    st.caption(
        "Source: [Onion Bhaji Recipe - Indian Healthy Recipes](https://www.indianhealthyrecipes.com/onion-bhaji/)"
    )
