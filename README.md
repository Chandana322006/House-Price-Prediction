# 🏠 House Price Prediction Using Linear Regression

A machine learning project that predicts house prices based on property features such as area, number of bedrooms, bathrooms, parking spaces, location preferences, and furnishing status. The project includes a Python prediction model and an interactive web application built using Streamlit.

## 📌 Project Overview

The goal of this project is to estimate house prices using historical housing data and Linear Regression, a supervised machine learning algorithm.

Users can enter house details through a simple web interface and receive an estimated house price.

## ✨ Features

- 📊 Housing dataset exploration and preprocessing
- 🤖 House price prediction using Linear Regression
- 🔢 Support for numerical and categorical features
- 📈 Model evaluation using Mean Absolute Error (MAE) and R² score
- 📉 Actual vs. predicted price visualization
- 🌐 Interactive Streamlit web application
- 🏡 User-friendly input fields and price prediction button

## 🛠️ Technologies Used

- **Python** — Programming language
- **Pandas** — Data manipulation and preprocessing
- **Scikit-learn** — Machine learning and model evaluation
- **Matplotlib** — Data visualization
- **Streamlit** — Interactive web application
- **VS Code** — Development environment

## 📂 Project Structure

```text
House-Price-Prediction/
│
├── Housing.csv
├── house_price.py
├── app.py
├── README.md
└── screenshots/
    ├── app-homepage.png
    ├── price-prediction.png
    └── actual-vs-predicted.png
```

## 📊 Dataset

The project uses `Housing.csv`, which contains housing records and property attributes.

Features include:

- Area
- Bedrooms and bathrooms
- Number of stories
- Main road access
- Guest room and basement availability
- Hot water heating
- Air conditioning
- Parking spaces
- Preferred area
- Furnishing status

**Target variable:** `price`

Categorical features are converted into numerical columns using one-hot encoding before model training.

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
cd House-Price-Prediction
```

Replace the placeholder with your actual GitHub repository URL.

### 2. Install the dependencies

```bash
python -m pip install pandas scikit-learn matplotlib streamlit
```

### 3. Run the Python model

```bash
python house_price.py
```

This runs the model training, evaluation, visualization, and interactive terminal prediction.

### 4. Launch the web application

```bash
python -m streamlit run app.py
```

Open the local URL displayed in the terminal, usually `http://localhost:8501`.

Enter the property details and click **Predict Price** to view the estimated price.

## 🧠 Machine Learning Approach

The project follows these steps:

1. Load the housing dataset using Pandas.
2. Inspect the dataset and prepare the input features.
3. Encode categorical variables using one-hot encoding.
4. Split the dataset into training and testing sets using an 80:20 ratio.
5. Train a Linear Regression model.
6. Generate predictions for the test dataset.
7. Evaluate the model and visualize actual versus predicted prices.
8. Use the trained model to estimate prices for new property details.

## 📈 Model Evaluation

The model was evaluated using a test dataset.

| Metric | Result |
|---|---:|
| Mean Absolute Error (MAE) | 970,043.40 |
| R² Score | 0.6529 |
| Training/Test Split | 80% / 20% |

**Interpretation:**

- **MAE:** The predictions differ from actual prices by approximately 970,043 price units on average.
- **R² Score:** The model explains approximately 65.3% of the variation in house prices in the test dataset.

These results provide a baseline for further improvement. Prediction errors can vary between individual houses.

## 🖼️ Screenshots

Add screenshots of your working application and model output to the `screenshots/` folder.

### 1. Streamlit Application

![Streamlit application screenshot](screenshots/app-homepage.png)

### 2. House Price Prediction Result

![House price prediction result](screenshots/price-prediction.png)

### 3. Actual vs. Predicted Prices

![Actual vs. predicted price graph](screenshots/actual-vs-predicted.png)

*Note: Replace these image paths with your actual screenshot filenames. The screenshots must be saved in the `screenshots/` folder for them to display on GitHub.*

## 🚀 Future Improvements

- Compare Linear Regression with Random Forest and other regression algorithms.
- Improve prediction accuracy through feature engineering and model tuning.
- Add input validation and more informative error messages.
- Deploy the Streamlit application online.
- Add more evaluation metrics and model comparison visualizations.

## 🎯 Learning Outcomes

Through this project, I gained practical experience in data preprocessing, supervised machine learning, model evaluation, data visualization, and building an interactive web application with Python.

## 👩‍💻 Author

**Chandana ML**

Electronics and Computer Engineering Student

GitHub: [Chandana322006](https://github.com/Chandana322006)

---

*This project is intended for educational purposes. Predicted prices are estimates and should not be treated as professional property valuations.*
