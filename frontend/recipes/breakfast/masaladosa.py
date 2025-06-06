import streamlit as st


def render():
    st.title("🥔 Masala Dosa Recipe")
    st.subheader("Crispy fermented crepes with a spiced potato filling")
    st.markdown(
        """
A popular South Indian breakfast or snack, this recipe guides you through making the batter and the flavorful potato masala.
"""
    )
    # Estimate total time and servings, acknowledging long fermentation
    st.info(
        "⏰ **Total Time**: Approx. 10 hrs (Fermentation) + 1 hr (Prep & Cook) | 👨‍🍳 **Yields**: Varies (many dosas) | ✍️ **Author**: Swasthi"
    )

    st.header("🥘 Ingredients")

    st.subheader("• For Masala Dosa Batter")
    st.markdown(
        """
- ½ cup urad dal (skinned black gram)
- 3 tablespoon chana dal (bengal gram) (or 2 tbsps chana dal & 1 tbsp toor dal)
- 1½ cup raw sona masuri rice
- ½ cup idli rice (optional, can skip or substitute with raw rice)
- 3 tablespoon poha (flattened rice)
- ½ teaspoon methi seeds (fenugreek seeds)
- ¾ teaspoon pink salt or non-iodized salt (or as needed)
- 1¼ cups water to blend dal (adjust if needed)
- ½ to ¾ cups water to blend rice
"""
    )

    st.subheader("• For Potato Masala (Curry)")
    st.markdown(
        """
- 2 cups potatoes cubed (500 grams or 3 medium)
- 1 tablespoon oil
- ¼ to ½ teaspoon mustard seeds
- ½ teaspoon cumin (jeera)
- 1 teaspoon chana dal (bengal gram) (optional)
- 1 teaspoon urad dal (skinned black gram) (optional)
- 1 pinch asafoetida (hing) (optional)
- 1 teaspoon ginger (grated or paste)
- ¾ to 1 cup onions thinly sliced
- 1 sprig curry leaves
- 2 green chilies chopped or sliced
- ¼ teaspoon turmeric (haldi)
- ½ to ¾ teaspoon salt (adjust to taste)
- 2 tablespoon coriander leaves finely chopped
"""
    )

    st.subheader("• To Make Dosas")
    st.markdown(
        """
- Butter as needed (preferably unsalted cultured butter)
"""
    )

    st.header("👨‍🍳 Instructions")

    st.subheader("• 1. Make Masala Dosa Batter")
    st.markdown(
        """
1.  **Rinse & Soak:** Add urad dal, chana dal, and methi seeds to a large bowl. Rinse them well a few times and pour lots of fresh water. In another bowl, add rice and rinse well, then pour lots of fresh water. Soak both for 4 to 5 hours. 30 minutes before blending, rinse poha twice, immerse in water, and soak for 30 minutes.
2.  **Blend Dal & Poha:** Drain water completely from dal and add to a blender jar along with poha. Pour 1¼ cup water and salt (if living in hot weather, add salt after fermentation). Blend until thick, frothy, and smooth. Ensure the blender doesn't overheat; blend in intervals. Transfer this batter to the bowl where you soaked the dal.
3.  **Blend Rice:** Drain water completely from rice and add it along with ½ cup water to the blender jar. Blend slightly coarse or smooth to your liking (a fine semolina texture is suggested). If needed, use the remaining ¼ cup water for blending.
4.  **Combine & Mix:** Pour the blended rice batter into the dal batter and mix well. Divide the batter into two large bowls if you plan to use it on different days. Cover the bowls.
"""
    )

    st.subheader("• 2. Fermentation")
    st.markdown(
        """
1.  Allow the masala dosa batter to ferment in a warm place for about 6 to 16 hours, depending on your climate. The batter should rise and turn slightly fluffy. Avoid over-fermenting.
2.  **For Cold Places:** Preheat oven to 60°C (140°F) for 10 minutes, then place batter inside with the oven light on. Alternatively, use an Instant Pot on yogurt settings.
"""
    )

    st.subheader("• 3. Make Potato Curry (Incomplete Instructions from Source)")
    st.markdown(
        """
1.  Boil or steam potatoes until just done. Do not cook them until very...
    *(The instructions for the potato curry were incomplete in the retrieved content from the source website. Please refer to the source for full details.)*
"""
    )

    st.subheader("• 4. To Make Dosas (Instructions Missing from Source)")
    st.markdown(
        """
    *(The instructions for making the dosas themselves were not fully retrieved from the source website. Please refer to the source for full details on how to spread and cook the dosas.)*
"""
    )

    st.header("📊 Nutrition Info (Approximate per Dosa)")
    st.markdown("Calories: 215kcal | Carbohydrates: 36g | Protein: 6g | Fat: 5g")

    st.caption(
        "Source: [Masala Dosa Recipe - Indian Healthy Recipes](https://www.indianhealthyrecipes.com/masala-dosa-recipe/#wprm-recipe-container-37664)"
    )
