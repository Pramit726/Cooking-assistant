import streamlit as st


def render():
    st.title("🍚 Rice Kheer (Chawal Ki Kheer) Recipe")
    st.subheader("Creamy, sweet, and aromatic Indian rice pudding")
    st.markdown(
        """
A traditional Indian dessert made with rice, milk, sugar, and flavored with cardamom and nuts.
A comforting and delightful treat for any occasion.
"""
    )
    # Estimate total time and servings based on the recipe details
    st.info(
        "⏰ **Total Time**: Approx. 55 mins | 👨‍🍳 **Serves**: 4-6 people | ✍️ **Author**: Swasthi"
    )

    st.header("🥘 Ingredients")

    st.subheader("• Main Ingredients")
    st.markdown(
        """
- 4 cups (1 liter) whole milk / full fat (for instant pot 2½ cups milk)
- ¼ cup water (to prevent burning)
- ¼ cup (50 grams) rice (basmati or any rice, or use ⅓ cup for faster cooking)
- 4 to 6 tablespoons (50 to 65 grams) organic sugar (4 tbsps for moderate sweetness)
"""
    )

    st.subheader("• Flavorings & Garnish (Optional)")
    st.markdown(
        """
- ½ teaspoon cardamom powder (or 2-3 pods powdered)
- ¼ cup unsalted nuts – cashews, pistachios (roughly chopped or silvered almonds)
- 2 tablespoons sweet raisins
- 1 tablespoon ghee (to fry nuts & raisins)
- 1 pinch saffron or 1 tsp edible rose water or few drops of kewra water
"""
    )

    st.header("👨‍🍳 Instructions")

    st.subheader("• 1. Prepare Rice & Milk Base")
    st.markdown(
        """
1.  Wash rice a few times until the water runs clear, then drain completely.
2.  Pour water and milk into a heavy-bottomed pot or Dutch oven. Bring it to a boil on medium heat.
3.  Stir in the washed rice.
"""
    )

    st.subheader("• 2. Cook the Kheer")
    st.markdown(
        """
1.  Continue to cook on a medium to low heat, stirring every 3 minutes to prevent scorching, until the rice is soft, completely cooked, and lightly mushy. This usually takes about 25 to 30 minutes.
2.  Stir in the sugar and continue to cook for about 10 minutes, until the kheer thickens but is still of a flowy consistency (it will thicken further upon cooling).
3.  Taste test and add more sugar if desired, simmering for an additional 5 minutes if more sugar is added.
"""
    )

    st.subheader("• 3. Add Flavorings & Finish")
    st.markdown(
        """
1.  Stir in cardamom powder, saffron (optional), rose water (optional), and chopped nuts.
2.  **Optional Garnish:** If you prefer ghee in your rice kheer, heat ghee in a small pan, fry the nuts until light golden, then stir in raisins until plump. Pour this over the kheer.
"""
    )

    st.header("📊 Nutrition Info (Approximate per serving)")
    st.markdown("Calories: 265kcal | Carbohydrates: 42g | Protein: 10g | Fat: 8g")

    st.caption(
        "Source: [Rice Kheer Recipe - Indian Healthy Recipes](https://www.indianhealthyrecipes.com/rice-kheer-recipe-chawal-ki-kheer/)"
    )
