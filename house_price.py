
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("Housing.csv")

# Separate input features and target
X = data.drop("price", axis=1)
y = data["price"]

# Convert categorical columns into numeric columns
X = pd.get_dummies(X, drop_first=True, dtype=int)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict house prices
y_pred = model.predict(X_test)

# Evaluate the model
print("Training records:", len(X_train))
print("Testing records:", len(X_test))
print("Mean Absolute Error:", mean_absolute_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))

# Compare actual and predicted prices
results = pd.DataFrame({
    "Actual Price": y_test.values,
    "Predicted Price": y_pred.round(2)
})

print("\nActual vs Predicted Prices:")
print(results.head())
plt.figure(figsize=(8, 5))

plt.scatter(y_test, y_pred, color="blue", alpha=0.7)

plt.xlabel("Actual House Price")
plt.ylabel("Predicted House Price")
plt.title("Actual vs Predicted House Prices")
plt.grid(True)
plt.tight_layout()
plt.show()
print("\n--- House Price Prediction ---")

area = float(input("Enter area in square feet: "))
bedrooms = int(input("Enter number of bedrooms: "))
bathrooms = int(input("Enter number of bathrooms: "))
stories = int(input("Enter number of stories: "))
mainroad = input("Is the house connected to the main road? (yes/no): ").lower()
guestroom = input("Does the house have a guest room? (yes/no): ").lower()
basement = input("Does the house have a basement? (yes/no): ").lower()
hotwaterheating = input("Does the house have hot water heating? (yes/no): ").lower()
airconditioning = input("Does the house have air conditioning? (yes/no): ").lower()
parking = int(input("Enter number of parking spaces: "))
prefarea = input("Is it in a preferred area? (yes/no): ").lower()
furnishingstatus = input(
    "Furnishing status (furnished/semi-furnished/unfurnished): "
).lower()

# Create input data
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

# Match the training columns
new_house = new_house.reindex(columns=X.columns, fill_value=0)

# Predict the price
predicted_price = model.predict(new_house)[0]
print(f"\nEstimated House Price: ₹{predicted_price:,.2f}")