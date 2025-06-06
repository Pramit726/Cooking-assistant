import streamlit as st


def render():
    st.title("🍩 Gulab Jamun Recipe (Milk Powder)")
    st.subheader(
        "Classic Indian sweet, soft and spongy milk-based dumplings in sugar syrup"
    )
    st.markdown(
        """
A simpler version of the beloved Indian dessert, made with milk powder for a quick and delicious treat.
"""
    )
    # Estimate total time and servings based on the recipe details
    st.info(
        "⏰ **Total Time**: Approx. 30 mins (plus 3 hrs soaking) | 👨‍🍳 **Yields**: 14-18 Gulab Jamuns | ✍️ **Author**: Swasthi"
    )

    st.header("🥘 Ingredients")

    st.subheader("• For the Gulab Jamun Dough")
    st.markdown(
        """
- 1 cup milk powder
- 5 tbsp all-purpose flour (maida)
- 1 tsp ghee or oil (for mixing into dough)
- 1 tbsp ghee or oil (for greasing hands)
- 2 to 4 tbsp milk (use as needed)
- 1 tbsp curd (yogurt) or ¾ tbsp lemon juice
- 1 large pinch of baking soda (or ⅛ tsp)
"""
    )

    st.subheader("• For Deep Frying")
    st.markdown(
        """
- Ghee or oil for deep frying
"""
    )

    st.subheader("• For Sugar Syrup")
    st.markdown(
        """
- 1¼ to 1½ cups sugar
- 1½ cup water
- 4 pods green cardamom (crushed) or ¼ tsp cardamom powder
- 1 tsp rose water
"""
    )

    st.subheader("• For Garnish")
    st.markdown(
        """
- 1 tsp pistachios, chopped
"""
    )

    st.header("👨‍🍳 Instructions")

    st.subheader("• 1. Prepare Sugar Syrup")
    st.markdown(
        """
1.  In a pot, combine water, sugar, and crushed cardamoms.
2.  Boil the syrup until it becomes slightly sticky.
3.  Turn off the stove before it reaches a 1-string consistency. If it does, add 2 tbsp of water and mix.
4.  Stir in rose water and set aside to keep warm/hot.
"""
    )

    st.subheader("• 2. Prepare Gulab Jamun Dough")
    st.markdown(
        """
1.  Fluff up the flour, then measure correctly.
2.  In a bowl, mix flour, milk powder, and baking soda. Sieve or mix uniformly.
3.  Add 1 tsp ghee/oil to the mixture and mix well.
4.  In a small bowl, mix lemon juice/yogurt with 2 tbsp milk.
5.  Pour 1.5 tbsp of this liquid mixture into the flour mixture.
6.  Gently bring the flour together to form a smooth dough. Add more milk/curd mixture sparingly if the dough is too dry, using only as needed. The dough will be sticky at first.
7.  Grease your fingers and make a ball with the dough. The dough should hold shape well and be smooth without cracks.
"""
    )

    st.subheader("• 3. Shape and Fry Gulab Jamuns")
    st.markdown(
        """
1.  Divide the dough into 14 to 18 equal-sized portions.
2.  Grease your hands and roll each portion into smooth balls. Ensure they are free of cracks, as cracks will appear on the fried gulab jamuns. Keep the balls covered.
3.  Heat ghee or oil in a pan on medium heat.
4.  Check syrup: Ensure it is hot but not boiling.
5.  **Test Oil Temperature:** Drop a small piece of dough into the oil. It should rise slowly without changing color. If it rises rapidly and browns, the oil is too hot; let it cool slightly.
6.  When the ghee/oil is medium hot, add the balls. Do not overcrowd.
7.  Fry the balls on a medium flame for 1-2 minutes, then reduce flame to low and continue frying until golden brown. Stir gently and continuously to ensure uniform frying.
"""
    )

    st.subheader("• 4. Soak and Serve")
    st.markdown(
        """
1.  Carefully transfer the hot fried gulab jamuns directly into the hot sugar syrup.
2.  Allow them to soak for at least 3 hours. They will absorb the syrup and become soft and spongy.
3.  Garnish with chopped pistachios before serving.
"""
    )

    # Nutrition info from the source page's recipe card.
    st.header("📊 Nutrition Info (Approximate per serving)")
    st.markdown("Calories: 247kcal | Carbohydrates: 43g | Protein: 3g | Fat: 9g")

    st.caption(
        "Source: [Gulab Jamun Recipe (Milk Powder) - Indian Healthy Recipes](https://www.indianhealthyrecipes.com/gulab-jamun-recipe-using-milk-powder/)"
    )
