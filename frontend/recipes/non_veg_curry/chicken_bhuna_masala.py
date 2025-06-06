import streamlit as st


def render():
    st.title("🌶️ Chicken Bhuna Masala Recipe")
    st.subheader("Rich, aromatic, and spicy dry chicken curry")
    st.markdown(
        """
A classic Indian dish where chicken is slow-cooked in its own juices with spices until the masala is rich and clinging to the meat.
"""
    )
    # Estimate total time and servings based on 1kg chicken and bhuna style cooking
    st.info(
        "⏰ **Total Time**: Approx. 1 hr | 👨‍🍳 **Serves**: 4-6 people | ✍️ **Author**: Swasthi"
    )

    st.header("🥘 Ingredients")

    st.subheader("• Chicken & Marinade")
    st.markdown(
        """
- 1 kg (2.2 lbs) chicken (curry cut or drumsticks & cut thighs)
- ½ to ¾ teaspoon salt
- ½ of combined ground spices (see below)
- 1 tablespoon Lemon juice
"""
    )

    st.subheader("• Whole Spices (for tempering)")
    st.markdown(
        """
- 1 bay leaf
- 1 to 2 black cardamoms
- 4 green cardamoms
- 4 cloves
- 2 inch cinnamon
- 2 dried red chilies (optional)
"""
    )

    st.subheader("• For the Masala Base")
    st.markdown(
        """
- ¼ cup oil
- 1 tablespoon ghee
- 2 cups chopped onions (2 medium)
- 1 to 2 green chilies (slit)
- 1 cup chopped tomatoes (or pureed, 1 medium tomato)
- 1½ tablespoon ginger garlic paste (divided ½ + 1 tbsp)
- ½ cup yogurt (fresh curd, not sour)
- 1½ tablespoon kasuri methi (dried fenugreek leaves)
- ¼ cup coriander leaves (fine chopped to garnish)
"""
    )

    st.subheader("• Ground Spices (combine these for use in marinade & masala)")
    st.markdown(
        """
- 1½ to 3 teaspoon Kashmiri Red chilli powder (adjust to taste)
- ¼ teaspoon turmeric powder
- 2 to 3 teaspoon garam masala (adjust to taste)
- 2 teaspoons coriander powder
- 1 teaspoon cumin powder
- 1 teaspoon fennel powder
- ½ to ¾ teaspoon black pepper (adjust to taste)
"""
    )

    st.header("👨‍🍳 Instructions")

    st.subheader("• Prep & Marinate Chicken")
    st.markdown(
        """
1.  In a bowl, combine all the ground spices.
2.  Add chicken to a mixing bowl. Sprinkle ½ to ¾ teaspoon salt, half of the combined ground spices, and lemon juice. Mix well to marinate. Cover and set aside (or refrigerate overnight).
3.  Chop onions, slit green chilies, deseed & chop tomatoes. Prepare ginger & garlic paste if not using pre-made.
"""
    )

    st.subheader("• Make Bhuna Masala Base")
    st.markdown(
        """
1.  Heat oil in a wok or pan on medium flame. Add onions and green chilies. Sauté on medium-high for 6-7 minutes, then medium-low until golden brown (do not burn).
2.  Add ginger garlic paste and sauté for 1 minute until raw smell disappears.
3.  Stir in the remaining half of the combined ground spices and sauté for 1 minute.
4.  Stir in chopped tomatoes and salt. Cook until tomatoes dry out, blend with onions, and oil begins to release.
5.  Take 2 tablespoons of the hot onion-tomato masala and mix it into the whisked yogurt until well combined.
6.  Reduce heat and slowly add this yogurt mixture to the pan. Sauté until the yogurt cooks down and the bhuna masala thickens.
"""
    )

    st.subheader("• Cook Chicken Bhuna")
    st.markdown(
        """
1.  In a separate pan, heat 1 tablespoon ghee. Add dried red chilies (if using) and fry for 30-40 seconds.
2.  Add all whole spices (bay leaf, black/green cardamoms, cloves, cinnamon). Be careful as they splutter.
3.  Transfer the marinated chicken to this pan. Fry on medium-high for 2-3 minutes, then medium-low for another 2-3 minutes. Turn off heat.
4.  Add the cooked bhuna chicken and 2 tablespoons of chopped coriander leaves (optional) to the main masala pan. Continue to sauté for 2-3 minutes.
5.  Cover and cook on a low heat until the chicken is fully cooked and tender. If the masala sticks, splash a little hot water (about ¼ cup) around the sides of the pan (not directly over the chicken).
6.  Taste and adjust salt. Sprinkle crushed kasuri methi. Garnish with remaining coriander leaves.
"""
    )

    # Nutrition info is generally available on the source page's recipe card.
    st.header("📊 Nutrition Info (Approximate per serving)")
    st.markdown("Calories: 430kcal | Carbohydrates: 19g | Protein: 43g | Fat: 22g")

    st.caption(
        "Source: [Chicken Bhuna Masala Recipe - Indian Healthy Recipes](https://www.indianhealthyrecipes.com/chicken-bhuna-masala/)"
    )
