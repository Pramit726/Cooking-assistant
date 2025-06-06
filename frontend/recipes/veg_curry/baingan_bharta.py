import streamlit as st


def render():
    st.title("🍆 Baingan Bharta Recipe")
    st.subheader("Smoky and flavorful roasted eggplant mash")
    st.markdown(
        """
A popular North Indian dish made by roasting eggplant over open flame (or oven/air fryer), peeling, mashing, and then cooking it with sautéed onions, tomatoes, ginger, garlic, and spices.
"""
    )
    # Estimate total time and servings based on the recipe details
    st.info(
        "⏰ **Total Time**: Approx. 35 mins | 👨‍🍳 **Serves**: 3-4 people | ✍️ **Author**: Swasthi"
    )

    st.header("🥘 Ingredients")

    st.subheader("• For Roasting Eggplant")
    st.markdown(
        """
- 500 grams (1.1 lbs.) eggplants (baingan, preferably large, round ones)
- 4 medium garlic cloves
- 1 to 2 green chilies (slit, adjust to taste)
- 1 teaspoon oil (mustard oil or any other, for brushing)
"""
    )

    st.subheader("• For the Masala")
    st.markdown(
        """
- 1½ tablespoons oil (mustard oil or any other)
- ½ cup (130 grams) onions (chopped)
- ¾ cup (200 grams) tomato (deseeded & chopped)
- 3 large garlic cloves (fine chopped)
- ½ to ¾ inch ginger (fine chopped)
- ½ teaspoon Kashmiri red chilli powder (adjust to taste)
- ¼ to ½ teaspoon garam masala
- ¾ teaspoon salt (adjust to taste)
- 2 tablespoon coriander leaves (fine chopped, for garnish)
- Lemon juice (optional, for serving)
"""
    )

    st.header("👨‍🍳 Instructions")

    st.subheader("• 1. Roast Eggplant")
    st.markdown(
        """
1.  Rinse eggplants well and pat dry. Make 4 slits on the brinjal and push 2 garlic cloves deep inside 2 slits. Push the slit green chilies into the other 2 slits. Brush the eggplants with 1 teaspoon oil.
2.  **Stovetop Method:** Using tongs, place the eggplant directly over a medium-high flame. Keep turning to all sides and grill until the skin is charred and the eggplant is completely roasted and cooked through (12-14 mins).
3.  **Oven Method:** Line a metal tray with foil. Halve each eggplant and place cut-side down (skin side up) on the tray. You can also place whole tomatoes in the same tray. Broil/Grill at 460°F (240°C) for 16-20 minutes.
4.  **Air Fryer Method:** Place whole/halved eggplant, chilies, garlic, and tomatoes (if desired) in the air fryer basket. Air fry at 400°F (200°C). Whole eggplant takes about 22 mins, halved takes about 16 mins.
5.  **Check Doneness:** Insert a fork into the eggplant; it should go in smoothly and easily, indicating it's soft and cooked.
6.  **Cool & Peel:** Let the eggplant cool slightly. Optionally, transfer to a bowl and cover for 5 minutes (this helps steam loosen the skin). Peel the charred skin.
7.  **Mash/Chop:** Mash or finely chop the roasted eggplant, grilled garlic, and grilled green chilies. Set aside. Also, finely chop the raw tomatoes, onions, and raw garlic.
"""
    )

    st.subheader("• 2. Prepare the Masala Base")
    st.markdown(
        """
1.  Pour 1½ tablespoons oil into a hot pan. Once hot, add fine chopped ginger and raw garlic. Sauté for 30-60 seconds until aromatic.
2.  Stir in the chopped onions and sauté until they turn light golden (6-7 minutes).
3.  Add the chopped tomatoes and salt. Cook until they become soft (5-6 minutes).
4.  Add Kashmiri red chili powder and cook for 1-2 minutes until the raw smell from the tomatoes is gone.
"""
    )

    st.subheader("• 3. Combine & Finish")
    st.markdown(
        """
1.  Stir in the mashed/chopped roasted eggplant, grilled garlic, and grilled green chilies. (You may want to save half of the green chilies for later after taste testing if you prefer less spice).
2.  Mix and mash a bit to blend everything well.
3.  Sauté for 7-8 minutes on medium heat.
4.  Stir in garam masala (if using). Turn off the stove.
5.  Taste test and adjust salt and green chili if required.
6.  Garnish generously with fine chopped coriander leaves. Squeeze some lemon juice if you like.
"""
    )

    st.subheader("• Serving Suggestion")
    st.markdown(
        """
- Serve hot with roti, rice, or naan.
"""
    )

    # Nutrition info from the source page's recipe card.
    st.header("📊 Nutrition Info (Approximate per serving)")
    st.markdown("Calories: 150kcal | Carbohydrates: 15g | Protein: 4g | Fat: 9g")

    st.caption(
        "Source: [Baingan Bharta - Indian Healthy Recipes](https://www.indianhealthyrecipes.com/baingan-bharta/)"
    )
