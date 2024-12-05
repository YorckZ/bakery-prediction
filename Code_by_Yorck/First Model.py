import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Load data
umsatzdaten_file = '../0_DataPreparation/umsatzdaten_gekuerzt.csv'
wetter_file = '../0_DataPreparation/wetter.csv'

# Convert data to pandas dataframes
umsatzdaten_df = pd.read_csv(umsatzdaten_file)
wetter_df = pd.read_csv(wetter_file)

# Merge dataframes via inner join on 'Datum'
merged_df = pd.merge(umsatzdaten_df, wetter_df, on='Datum', how='inner')

# Drop rows with missing values
merged_df = merged_df.dropna()

# Select feature and target variable
X = merged_df[['Temperatur']]  # Feature
y = merged_df['Umsatz']  # Target

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


# Predict sales for a single temperature value
# input_temperature = [[20]]
# predicted_umsatz = model.predict(input_temperature)
# print(f"Predicted Umsatz for temperature {input_temperature[0][0]}: {predicted_umsatz[0]}")


# Predict sales for temperature values 0 to 30
results = {}
for i in range(31):
    input_temperature = pd.DataFrame([[i]], columns=['Temperatur'])
    predicted_umsatz = model.predict(input_temperature)
    results[i] = round(predicted_umsatz[0], 2)
    # print(i, predicted_umsatz[0])
# print(results)


# Visualize predictions on a matplotlib
# Extract x and y values from results
x_values = list(results.keys())
y_values = list(results.values())

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, marker='o', linestyle='-', label='Predicted Umsatz')

# Add labels, title, and legend
plt.xlabel('Temperature (°C)')
plt.ylabel('Predicted Sales (€)')
plt.title('Predicted Sales vs. Temperature')
plt.legend()

# Display the plot
plt.grid(True)
plt.show()
