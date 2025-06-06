import streamlit as st


def render():
    st.title("🥔🥦 Aloo Gobi Recipe")
    st.subheader("Classic Indian dry curry with potatoes and cauliflower")
    st.markdown(
        """
A popular and comforting vegetarian dish made with tender potatoes and cauliflower florets cooked with aromatic Indian spices.
"""
    )
    # Estimate total time and servings based on the recipe details
    st.info(
        "⏰ **Total Time**: Approx. 50 mins | 👨‍🍳 **Serves**: 3-4 people | ✍️ **Author**: Swasthi"
    )

    st.header("🥘 Ingredients")

    st.subheader("• Main Ingredients")
    st.markdown(
        """
- 1½ cup (2 medium) potatoes (cubed to ¾ x ¾ inch)
- 2 cups (180 grams) cauliflower florets (gobi, chopped to 1½ inch)
"""
    )

    st.subheader("• Aromatics & Fresh Ingredients")
    st.markdown(
        """
- ¾ to 1 cup (1 medium) onion (chopped finely)
- ¾ to 1 cup (2 medium) tomatoes (finely chopped) or ¼ cup tomato puree / 2 tbsp tomato paste mixed with 3 tbsps water
- ½ tablespoon (½ inch) ginger, peeled & minced or grated
- ½ tablespoon (3 to 4) garlic cloves, peeled & minced or pressed
- 1 green chili, slit or chopped (optional)
- 2 tablespoons coriander leaves, chopped finely
- ½ to ¾ teaspoon salt (adjust to taste)
- 2 to 3 tablespoons oil
- Lemon juice to serve (optional)
"""
    )

    st.subheader("• Spices")
    st.markdown(
        """
- ½ teaspoon cumin seeds (jeera)
- ¾ to 1¼ teaspoon Kashmiri red chili powder (adjust to taste)
- ¼ teaspoon turmeric
- 1 to 1½ teaspoon garam masala (adjust to taste)
- ¾ to 1 teaspoon coriander powder
- ½ to ¾ teaspoon roasted cumin powder (jeera powder)
- 1 tablespoon kasuri methi (dried fenugreek leaves) (optional)
- ½ to 1 teaspoon amchur (Optional, Dried mango powder)
"""
    )

    st.header("👨‍🍳 Instructions")

    st.subheader("• 1. Prepare Vegetables")
    st.markdown(
        """
1.  Chop cauliflower florets into 1½ inch pieces. Add them to slightly hot water and let sit for 3-4 minutes. Drain and rinse them well, then drain completely.
2.  Cube potatoes to ¾ x ¾ inch (or slice to ¾ inch thickness). Keep them immersed in a bowl of water until ready to use; this helps them cook faster.
3.  Mince ginger and garlic and set aside.
"""
    )

    st.subheader("• 2. Sauté Aromatics & Potatoes")
    st.markdown(
        """
1.  Heat oil in a pan and add cumin seeds. Once they sizzle, add minced ginger and garlic and sauté for 30 seconds.
2.  Add the chopped onions and stir-fry until they become transparent.
3.  Add the cubed potatoes and green chili (if using). Stir-fry for 2-3 minutes.
4.  Cover and cook on a low to medium heat until the potatoes are half-done. You can splash a little water if needed to help them cook faster. Stir occasionally while cooking covered.
"""
    )

    st.subheader("• 3. Add Cauliflower & Spices")
    st.markdown(
        """
1.  When potatoes are slightly tender but still undercooked, add the cauliflower florets and stir-fry for about 3 minutes.
2.  Add red chili powder, turmeric, roasted cumin powder, garam masala, and coriander powder. Mix well to coat the vegetables.
3.  Sprinkle 2-3 tablespoons of water all over the aloo gobi or along the sides of the pan and mix well. This step keeps the dish moist.
"""
    )

    st.subheader("• 4. Cook & Finish")
    st.markdown(
        """
1.  Cover and cook, stirring every few minutes, until both potatoes and cauliflower are almost fork-tender.
2.  Add salt and continue to cook covered on a low flame until the potatoes are soft and fully cooked. The vegetables will release moisture and cook quickly at this stage. Keep an eye not to overcook the cauliflower; it should remain slightly crunchy yet cooked.
3.  Next, add the finely chopped tomatoes and kasuri methi. Fry on a medium to high flame until the raw smell of tomatoes disappears (about 2-4 minutes). Add a little oil at this stage if needed.
4.  Sprinkle amchur (if using).
5.  Finally, garnish with fresh coriander leaves. Sprinkle some lemon juice if desired before serving.
6.  Serve hot with rice, roti, or any Indian bread.
"""
    )

    st.header("📊 Nutrition Info (Approximate per serving)")
    st.markdown("Calories: 260kcal | Carbohydrates: 30g | Protein: 7g | Fat: 14g")

    st.caption(
        "Source: [Aloo Gobi Recipe - Indian Healthy Recipes](https://www.indianhealthyrecipes.com/aloo-gobi-recipe/)"
    )
