import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load data
umsatzdaten_file = '../0_DataPreparation/umsatzdaten_gekuerzt.csv'
wetter_file = '../0_DataPreparation/wetter.csv'

umsatzdaten_df = pd.read_csv(umsatzdaten_file)
wetter_df = pd.read_csv(wetter_file)

# Merge datasets via inner join on 'Datum'
merged_df = pd.merge(umsatzdaten_df, wetter_df, on='Datum', how='inner')

# Drop rows with missing values
merged_df = merged_df.dropna()

# Select feature and target variable
X = merged_df[['Temperatur']]  # Feature
y = merged_df['Umsatz']        # Target

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Print the results
print("Model Coefficient:", model.coef_[0])
print("Model Intercept:", model.intercept_)
print("Mean Squared Error:", mse)
print("R-squared:", r2)
