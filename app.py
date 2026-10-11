
import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

st.set_page_config(page_title="House Price Predictor", page_icon="🏠")

st.title("🏠 House Price Prediction")
st.write("Enter the house details to estimate its price.")

# Load and train the model
data = pd.read_csv("Housing.csv")
X = pd.get_dummies(data.drop("price", axis=1), drop_first=True, dtype=int)
y = data["price"]

model = LinearRegression()
model.fit(X, y)

# User inputs
area = st.number_input("Area (square feet)", min_value=1, value=3000)
bedrooms = st.number_input("Number of bedrooms", min_value=1, max_value=10, value=3)
bathrooms = st.number_input("Number of bathrooms", min_value=1, max_value=10, value=2)
stories = st.number_input("Number of stories", min_value=1, max_value=4, value=2)

mainroad = st.selectbox("Main road access", ["yes", "no"])
guestroom = st.selectbox("Guest room", ["no", "yes"])
basement = st.selectbox("Basement", ["no", "yes"])
hotwaterheating = st.selectbox("Hot water heating", ["no", "yes"])
airconditioning = st.selectbox("Air conditioning", ["yes", "no"])
parking = st.number_input("Parking spaces", min_value=0, max_value=5, value=1)
prefarea = st.selectbox("Preferred area", ["yes", "no"])
furnishingstatus = st.selectbox(
    "Furnishing status",
    ["furnished", "semi-furnished", "unfurnished"]
)

# Prepare input in the same format as training data
new_house = pd.DataFrame([{
    "area": area,
    "bedrooms": bedrooms,
    "bathrooms": bathrooms,
    "stories": stories,
    "mainroad": mainroad,
    "guestroom": guestroom,
    "basement": basement,
    "hotwaterheating": hotwaterheating,
    "airconditioning": airconditioning,
    "parking": parking,
    "prefarea": prefarea,
    "furnishingstatus": furnishingstatus
}])

new_house = pd.get_dummies(new_house, drop_first=True, dtype=int)
new_house = new_house.reindex(columns=X.columns, fill_value=0)

if st.button("Predict Price"):
    predicted_price = model.predict(new_house)[0]
    st.success(f"Estimated House Price: ₹{predicted_price:,.0f}")
    st.caption("This is a model estimate, not a guaranteed market price.")
