import streamlit as st


def render():
    st.title("🥣 Upma Recipe")
    st.subheader("Quick and savory South Indian breakfast made with semolina")
    st.markdown(
        """
A wholesome and easy-to-make dish, Upma is a staple breakfast in many Indian households, customizable with vegetables and nuts.
"""
    )
    # Estimate total time and servings based on the recipe details
    st.info(
        "⏰ **Total Time**: Approx. 20-30 mins | 👨‍🍳 **Serves**: 2-3 people | ✍️ **Author**: Swasthi"
    )

    st.header("🥘 Ingredients")

    st.subheader("• Main Ingredient")
    st.markdown(
        """
- 1 cup Rava (Bombay rava / sooji / semolina)
"""
    )

    st.subheader("• For Tempering")
    st.markdown(
        """
- 2 to 2½ tablespoons oil or ghee
- ½ teaspoon mustard seeds
- ½ teaspoon cumin seeds (optional)
- 1 teaspoon split urad dal (skinned split black gram)
- 1½ teaspoon chana dal (optional, Bengal gram)
- 2 tablespoons peanuts (optional)
- 8 to 12 cashews (optional, can omit if using peanuts)
- 1 sprig curry leaves
- 1 pinch asafoetida (hing) (optional)
"""
    )

    st.subheader("• Other Ingredients")
    st.markdown(
        """
- ¼ cup onion (chopped or sliced thinly)
- 1 to 2 green chilies, slit
- ½ inch ginger (½ to ¾ teaspoon minced or grated) (optional)
- 3 cups water (2¾ cups for a drier upma)
- ½ to ¾ teaspoon salt
- 2 teaspoon ghee (optional, for finishing)
- Lemon juice (optional) to serve
"""
    )

    st.subheader("• Optional Additions")
    st.markdown(
        """
- ½ cup mixed vegetables (fine chopped carrots, beans, and green peas)
"""
    )

    st.header("👨‍🍳 Instructions")

    st.subheader("• 1. Roast Rava")
    st.markdown(
        """
1.  On medium heat, dry roast rava in a pan, stirring often, until it becomes crunchy and aromatic. Do not let it brown.
2.  Remove the roasted rava to a bowl and set aside to cool down.
"""
    )

    st.subheader("• 2. Temper Spices & Sauté Aromatics")
    st.markdown(
        """
1.  Pour oil into the hot pan. Add mustard seeds, cumin seeds (if using), urad dal, and chana dal (if using). Fry until the dals turn light golden.
2.  Add cashews (if using) and fry until they turn golden and aromatic.
3.  Stir in hing (if using), green chilies, ginger (if using), and curry leaves. Sauté for about 1 minute.
4.  Add chopped onions. Sauté until they turn transparent.
5.  If using mixed vegetables, add them now. Stir and cook covered until they are slightly tender.
"""
    )

    st.subheader("• 3. Boil Water & Combine")
    st.markdown(
        """
1.  Pour water into the pan and add salt. Mix well and taste the water; it should be slightly salty. Add more salt if needed.
2.  Bring the water to a rolling boil.
3.  Lower the heat to the lowest setting. With one hand, slowly pour the roasted rava in a thin stream into the boiling water, while continuously stirring with the other hand to incorporate it and prevent lumps. Be quick at this stage. Stir everything once to check for any lumps and break them up if found.
"""
    )

    st.subheader("• 4. Finish Cooking")
    st.markdown(
        """
1.  Cover the pan and cook on the lowest flame until all the water is completely absorbed. This typically takes 2 to 4 minutes depending on your pot/pan.
2.  Add 2 teaspoons of ghee (optional) and give a quick stir.
3.  Turn off the heat and cover the pan again to let the upma rest for 5 minutes.
"""
    )

    st.subheader("• 5. Serve")
    st.markdown(
        """
1.  Stir in lemon juice (optional) just before serving.
2.  Serve rava upma plain or with spiced peanut podi, chutney, pickle, or curd.
3.  Garnish with roasted/fried peanuts (if prepared separately).
"""
    )

    st.header("📊 Nutrition Info (Approximate per serving)")
    st.markdown("Calories: 280kcal | Carbohydrates: 40g | Protein: 7g | Fat: 10g")

    st.caption(
        "Source: [Upma Recipe - Indian Healthy Recipes](https://www.indianhealthyrecipes.com/upma-recipe-how-to-make-upma/)"
    )
