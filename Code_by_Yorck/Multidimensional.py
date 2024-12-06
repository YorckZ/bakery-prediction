import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
# from sklearn.preprocessing import OneHotEncoder
# from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


# Load data
umsatzdaten_file = '../0_DataPreparation/umsatzdaten_gekuerzt.csv'
wetter_file = '../0_DataPreparation/wetter.csv'

umsatzdaten_df = pd.read_csv(umsatzdaten_file)
wetter_df = pd.read_csv(wetter_file)

# Merge datasets via inner join on 'Datum'
merged_df = pd.merge(umsatzdaten_df, wetter_df, on='Datum', how='inner')

# Drop rows with missing values
merged_df = merged_df.dropna()

# Ensure the data is sorted by date
merged_df = merged_df.sort_values(by='Datum')

# Define training and validation datasets
train_end_date = '2017-07-31'
train_data = merged_df[merged_df['Datum'] <= train_end_date]
validation_data = merged_df[(merged_df['Datum'] > train_end_date)]

# Select features and target variable for training and validation
X_train = train_data[['Temperatur', 'Windgeschwindigkeit']]  # Features for training
y_train = train_data['Umsatz']                               # Target for training

X_test = validation_data[['Temperatur', 'Windgeschwindigkeit']]  # Features for validation
y_test = validation_data['Umsatz']                              # Target for validation

# Create a pipeline to handle preprocessing and regression
pipeline = Pipeline(steps=[
    ('scaler', StandardScaler()),  # Standardize features
    ('regressor', LinearRegression())  # Linear Regression model
])

# Train the model
pipeline.fit(X_train, y_train)

# Make predictions on validation data
y_pred = pipeline.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Print the results
print("Model Coefficients:", pipeline.named_steps['regressor'].coef_)
print("Model Intercept:", pipeline.named_steps['regressor'].intercept_)
print("Mean Squared Error:", mse)
print("R-squared:", r2)

# Example: Predict Umsatz for a specific date and wind speed
example_input = pd.DataFrame([[10, 0]], columns=['Temperatur', 'Windgeschwindigkeit'])
predicted_umsatz = pipeline.predict(example_input)
print(f"Predicted Umsatz: {predicted_umsatz[0]}")
