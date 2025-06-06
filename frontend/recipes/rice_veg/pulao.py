import streamlit as st


def render():
    st.title("🍚 Veg Pulao Recipe")
    st.subheader("Aromatic and flavorful Indian-style rice pilaf with vegetables")
    st.markdown(
        """
A wholesome and delicious one-pot meal made with basmati rice, mixed vegetables, and aromatic spices.
Perfect for a quick lunch or dinner.
"""
    )
    # Estimate total time and servings based on the recipe details
    st.info(
        "⏰ **Total Time**: Approx. 1 hr (includes soaking) | 👨‍🍳 **Serves**: 3-4 people | ✍️ **Author**: Swasthi"
    )

    st.header("🥘 Ingredients")

    st.subheader("• Basic Ingredients")
    st.markdown(
        """
- 1½ cups basmati rice (aged rice)
- 2 tablespoons oil or ghee
- Salt as needed
- Water (2½ cups for pressure cooker, 2¾ cups for pot, 1¾ cups for Instant Pot)
- 1½ teaspoons ginger garlic paste
"""
    )

    st.subheader("• Vegetables & Herbs")
    st.markdown(
        """
- 1 medium onion (thinly sliced)
- 2 green chilies (slit or as needed)
- 1 medium carrot (¾ cup chopped)
- 4 medium french beans (½ cup chopped to 1 inch)
- ½ cup green peas
- 1 small potato (cubed, optional)
- 3 tablespoons mint (pudina, finely chopped) (or coriander leaves)
"""
    )

    st.subheader("• Whole Spices")
    st.markdown(
        """
- 1 bay leaf (tej patta)
- ¾ teaspoon shahi jeera (caraway seeds, substitute cumin seeds)
- 4 green cardamoms (elaichi)
- 4 cloves (laung)
- 2 inch cinnamon (dalchini)
- 1 star anise (chakri phool) (optional, but recommended)
- 1 strand mace (javithri, optional)
- 1 pinch nutmeg (jaiphal) (optional)
- 2 pinches stone flower (dagad phool – optional)
- ½ teaspoon fennel seeds powder (saunf powder – optional)
"""
    )

    st.header("👨‍🍳 Instructions (Pot or Pressure Cooker Method)")
    st.markdown(
        """
1.  **Prepare Rice:** Rinse basmati rice a few times until water runs clear. Soak for at least 20 minutes, then drain completely.
2.  **Prepare Veggies & Herbs:** While rice soaks, rinse and chop carrots, beans, peas, potatoes. Slice onions, slit green chilies, and fine chop mint leaves.
3.  **Sauté Spices & Aromatics:** On medium flame, heat 2 tablespoons ghee or oil in a pot or pressure cooker. Add all whole spices. Once they sizzle, add sliced onions and chilies. Sauté until onions turn golden.
4.  **Add Ginger Garlic & Veggies:** Next, sauté ginger garlic paste for 30-60 seconds until raw smell disappears. Add all the chopped veggies and mint. Sauté for 2-3 minutes.
5.  **Add Water & Salt:** Pour in the required water (2½ cups for pressure cooker, 2¾ cups for pot) and add salt. Taste the water; it should be slightly salty. Bring to a rolling boil.
6.  **Add Rice & Cook:** Add the drained rice and stir gently.
    * **Pot Method:** Cover and cook on low heat until all water is absorbed and rice is cooked. Turn off stove. Cover and rest for 10-15 mins for fluffy grains.
    * **Pressure Cooker Method:** Cover with lid. Cook on medium-high flame for 1 whistle. Switch off stove. When pressure releases, remove lid and fluff with a fork.
7.  **Serve:** Serve hot or warm with raita or gravy.
"""
    )

    st.header("👨‍🍳 Instructions (Instant Pot Method)")
    st.markdown(
        """
1.  **Sauté Spices & Aromatics:** Press SAUTE. Add ghee/oil. Sauté whole spices for 30 seconds. Fry onions and green chilies until transparent (2 mins), then ginger garlic paste for 30 seconds.
2.  **Add Veggies, Rice & Water:** Add chopped veggies and mint. Saute for 2 mins. Add drained rice (1½ cups) and salt. Press CANCEL.
3.  **Cook in Instant Pot:** Pour 1¾ cups water and mix. Scrape bottom gently. Secure lid. Press PRESSURE COOK (high pressure) and set timer for 5 mins. Position steam release handle to sealing.
4.  **Release Pressure & Serve:** Instant Pot will beep when done. Let pressure release naturally for 5 mins. Manually release remaining pressure. Fluff with a fork and serve with yogurt raita.
"""
    )

    # Nutrition info is generally available on the source page's recipe card.
    st.header("📊 Nutrition Info (Approximate per serving)")
    st.markdown("Calories: 337kcal | Carbohydrates: 60g | Protein: 7g | Fat: 7g")

    st.caption(
        "Source: [Pulao Recipe - Indian Healthy Recipes](https://www.indianhealthyrecipes.com/pulao-recipe-veg-pulao-recipe/)"
    )
