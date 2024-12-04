import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
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

# Extract date-related features
merged_df['Datum'] = pd.to_datetime(merged_df['Datum'])
merged_df['DayOfYear'] = merged_df['Datum'].dt.dayofyear
merged_df['Weekday'] = merged_df['Datum'].dt.weekday

# Select features and target variable
# X = merged_df[['DayOfYear', 'Weekday', 'Windgeschwindigkeit']]  # Features
X = merged_df[['Temperatur', 'Windgeschwindigkeit']]  # Features
y = merged_df['Umsatz']  # Target

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a pipeline to handle preprocessing and regression
pipeline = Pipeline(steps=[
    ('scaler', StandardScaler()),  # Standardize features
    ('regressor', LinearRegression())  # Linear Regression model
])

# Train the model
pipeline.fit(X_train, y_train)

# Make predictions
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
example_input = [[2, 4]]  # Day of Year 150, Weekday 2 (Tuesday), Windgeschwindigkeit 15
predicted_umsatz = pipeline.predict([example_input])

print(f"Predicted Umsatz: {predicted_umsatz[0]}")
