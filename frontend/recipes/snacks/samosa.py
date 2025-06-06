import streamlit as st


def render():
    st.title("🥟 Samosa Recipe")
    st.subheader("Classic crispy pastry with a savory potato and pea filling")
    st.markdown(
        """
Learn how to make perfect samosas at home, with options for deep-frying, baking, or air-frying.
"""
    )
    # Estimate total time and servings based on the complexity of making samosas
    st.info(
        "⏰ **Total Time**: Approx. 55 mins | 👨‍🍳 **Yields**: 10 samosas | ✍️ **Author**: Swasthi"
    )

    st.header("🥘 Ingredients")

    st.subheader("• For the Dough")
    st.markdown(
        """
- 2 cups all-purpose flour (maida)
- ¾ teaspoon ajwain (carom seeds)
- ¾ teaspoon salt
- ¼ cup oil or ghee (4 tablespoons)
- 4-6 tablespoons water (as needed)
"""
    )

    st.subheader("• For the Potato Filling")
    st.markdown(
        """
- 4 medium (500 grams) potatoes
- ½ cup green peas (boiled or frozen)
- 1 tablespoon oil or ghee
- 1 tablespoon ginger (minced or paste)
- 1 to 2 green chilies (chopped, optional)
- 1 pinch hing (asafoetida) (optional)
- 4 tablespoons coriander leaves (chopped finely)
- 1 teaspoon lemon juice (or ½ tsp amchur or chaat masala)
- ½ teaspoon salt (adjust to taste)
"""
    )

    st.subheader("• Spices for Filling")
    st.markdown(
        """
- ¾ teaspoon cumin seeds
- ¾ to 1 teaspoon garam masala
- ¾ teaspoon red chilli powder (adjust to taste)
- ½ teaspoon cumin powder
- ½ teaspoon fennel powder (optional)
"""
    )

    st.subheader("• To Serve")
    st.markdown(
        """
- Mint Chutney
- Tamarind Chutney
"""
    )

    st.header("👨‍🍳 Instructions")
    st.markdown(
        """
1.  **Boil Potatoes:** Peel, halve, and boil potatoes until fork-tender. Cool and crumble.
2.  **Make Dough:** In a bowl, mix flour, carom seeds, salt, and oil. Rub with fingers for 3-4 minutes until it resembles breadcrumbs. Gradually add water to form a stiff, pliable dough. Cover and rest for 25-30 minutes.
3.  **Make Potato Filling:** Heat oil in a pan. Add cumin seeds, then ginger and green chilies. Stir in green peas and sauté for 2 minutes. Add spice powders and sauté for 30 seconds. Add crumbled potatoes and salt, mix well, and sauté for 2-3 minutes. Stir in coriander leaves and let cool. Add lemon juice if using.
4.  **Shape Samosas:** Knead dough and divide into 5 portions. Roll each into an oval disc (approx. 8.5x6.5 inches). Cut each disc into two semicircles. Apply water to the straight edge of one semicircle, form a cone, and seal. Fill with potato masala. Apply water to edges and seal, making a pleat on one side for a standing samosa. Ensure good seal and cover shaped samosas to prevent drying.
5.  **Deep Fry:** Heat oil until moderately hot. Fry samosas on low flame for 10-12 minutes until crust firms. Increase flame to medium, fry until golden and crispy. Remove to a wire rack.
6.  **Bake (Optional):** Preheat oven to 360°F (180°C). Brush samosas with oil and bake for 35-40 minutes.
7.  **Air Fry (Optional):** Preheat air fryer to 360°F (180°C). Place samosas in basket, spray with oil, and air fry for 12 minutes. Turn and air fry for another 5-6 minutes until golden and crisp.
8.  **Serve:** Serve hot with mint chutney and tamarind chutney.
"""
    )

    # Nutrition info is generally available on the source page's recipe card.
    st.header("📊 Nutrition Info (Approximate per Samosa)")
    st.markdown("Calories: 260kcal | Carbohydrates: 31g | Protein: 6g | Fat: 12g")

    st.caption(
        "Source: [Samosa Recipe - Indian Healthy Recipes](https://www.indianhealthyrecipes.com/samosa-recipe-make-samosa/)"
    )
