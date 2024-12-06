import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


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

# Convert to datetime if not already
merged_df['Datum'] = pd.to_datetime(merged_df['Datum'])

# Ensure the data is sorted by date
merged_df = merged_df.sort_values(by='Datum')

# Define your date thresholds
train_end_date = '2017-07-31'

# Split the data based on the date thresholds
train_data = merged_df[merged_df['Datum'] <= train_end_date]
validation_data = merged_df[(merged_df['Datum'] > train_end_date)]

# Define training and validation datasets
X_train = train_data[['Temperatur']]  # Feature for training
y_train = train_data['Umsatz']       # Target for training

X_test = validation_data[['Temperatur']]  # Feature for validation
y_test = validation_data['Umsatz']        # Target for validation

# Create and train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions on validation data
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

# Visualize predictions on a matplotlib
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
