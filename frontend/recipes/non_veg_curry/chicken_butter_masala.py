import streamlit as st


def render():
    st.title("🧈 Chicken Butter Masala Recipe")
    st.subheader("Creamy, rich, and mildly spiced Indian chicken curry")
    st.markdown(
        """
A popular and classic Indian dish with tender chicken cooked in a luscious, tomato-based gravy enriched with butter and cream.
"""
    )
    # Estimate total time and servings based on the recipe details
    st.info(
        "⏰ **Total Time**: Approx. 1 hr 45 mins (includes marination) | 👨‍🍳 **Serves**: 3-4 people | ✍️ **Author**: Swasthi"
    )

    st.header("🥘 Ingredients")

    st.subheader("• For the Chicken Marinade")
    st.markdown(
        """
- ½ cup Greek yogurt (hung curd / strained yogurt)
- 600 grams chicken thighs (boneless, ¾ inch pieces)
- ½ to 1 teaspoon Kashmiri red chilli powder
- ⅛ teaspoon turmeric
- 1 teaspoon garam masala
- ⅓ teaspoon salt
- 1 tablespoon ginger garlic paste
- 1 teaspoon kasuri methi (dried fenugreek leaves)
- 1 tablespoon oil
- 1 tablespoon lemon juice
"""
    )

    st.subheader("• For the Puree (Gravy Base)")
    st.markdown(
        """
- 1 tablespoon oil
- 1½ cup sliced onions (1 large, 120 grams)
- 15 grams ginger (peeled, 1½ tablespoons chopped)
- 15 grams garlic (1½ tablespoons chopped)
- 1 teaspoon salt (adjust to taste)
- 1½ to 2 teaspoon Kashmiri red chilli powder
- 5 cups tomatoes (chopped – 625 grams, 5 large or 14 oz can diced/fire roasted)
- 22 to 28 whole cashews (35 to 40 grams, ¼ to ⅓ cup)
- 1 teaspoon cumin powder (optional)
- 2 teaspoon coriander powder
- 1½ teaspoon garam masala (adjust to taste)
- 1½ teaspoon sugar
- ¼ to ¾ teaspoon cardamom powder
- 1½ cups water (for blending)
"""
    )

    st.subheader("• For Finishing the Butter Masala")
    st.markdown(
        """
- 2 to 3 tablespoons butter
- 1 green chilli (optional)
- ¼ to ½ teaspoon Kashmiri red chilli powder (optional)
- 1 cup hot water (divided, ½ + ½ cup)
- 1 tablespoon ghee
- ½ teaspoon garam masala
- 2 teaspoon kasuri methi (dried fenugreek leaves)
- ⅓ cup chilled cream (80 to 100 ml heavy cream or cooking cream)
- Fresh coriander leaves (fine chopped, for garnish)
"""
    )

    st.header("👨‍🍳 Instructions")

    st.subheader("• 1. Marinate Chicken")
    st.markdown(
        """
1.  Cut chicken into ¾ inch pieces and pat dry.
2.  In a bowl, combine all marinade ingredients: Greek yogurt, red chilli powder, turmeric, garam masala, salt, ginger garlic paste, kasuri methi, oil, and lemon juice.
3.  Add chicken and mix well. Marinate covered for a minimum of 60 minutes (overnight in the refrigerator is best).
"""
    )

    st.subheader("• 2. Prepare the Gravy Puree")
    st.markdown(
        """
1.  Heat a pan with 1 tablespoon oil. Sauté sliced onions until transparent (pink) and they lose their raw flavor.
2.  Add chopped ginger and garlic. Sauté for 2-3 minutes.
3.  Lower heat and stir in 1½ to 2 teaspoon Kashmiri red chilli powder.
4.  Add chopped tomatoes, cashews, and 1 teaspoon salt. Cook on medium-high heat until tomatoes break down to a mush.
5.  Stir in garam masala, cumin powder (optional), coriander powder, sugar, and cardamom powder. Turn off heat and let cool.
6.  Pour 1 cup water into a blender with the cooled mixture and blend until super smooth. If needed, add up to ½ cup more water for blending.
"""
    )

    st.subheader("• 3. Cook Chicken Butter Masala")
    st.markdown(
        """
1.  Wipe the pan clean and heat it with 2-3 tablespoons butter on low to medium heat.
2.  As butter melts, stir in green chilli (optional) and ¼ to ½ teaspoon red chilli powder (optional, adjust based on puree's spice level).
3.  Strain the smooth puree directly into the pan. (Ensure pan is not too hot to prevent spices from burning).
4.  Pour ½ cup hot water and simmer the butter masala until it thickens to a creamy consistency.
5.  **Grill Chicken:** While masala simmers, heat a separate pan/skillet with 1 tablespoon oil. Once hot, layer chicken pieces and cook on high heat until browned and slightly charred on both sides. Chicken may not be fully cooked.
6.  **Combine & Simmer:** When the butter masala is thick and creamy, add another ½ cup hot water (to rehydrate chicken) and 1 tablespoon ghee. Stir in the grilled chicken.
7.  Simmer for 3-4 minutes until chicken is cooked through and the butter masala reaches a thick, creamy consistency.
8.  **Finish:** Taste and adjust salt. Add ½ teaspoon garam masala and 2 teaspoons crushed kasuri methi.
9.  Stir in ⅓ cup chilled cream. Turn off the heat and let rest for at least 5 minutes.
"""
    )

    st.subheader("• To Serve")
    st.markdown(
        """
1.  Garnish with a tablespoon of cream and fine chopped coriander leaves.
2.  Serve hot with Butter Naan, Jeera Rice, or plain Basmati Rice.
"""
    )

    # Nutrition info from the source page's recipe card.
    st.header("📊 Nutrition Info (Approximate per serving)")
    st.markdown("Calories: 609kcal | Carbohydrates: 25g | Protein: 43g | Fat: 39g")

    st.caption(
        "Source: [Chicken Butter Masala - Indian Healthy Recipes](https://www.indianhealthyrecipes.com/chicken-butter-masala/)"
    )
