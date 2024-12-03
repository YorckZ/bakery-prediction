# Folie 19
# Beispiel Datensatzteilung (Zeitreihe)

import pandas as pd

# Sample data
data = pd.DataFrame({
'date': pd.date_range(start='2021-01-01', periods=100, freq='D'),
'value': range(100)
})

# Ensure the data is sorted by date
data = data.sort_values(by='date')
print (data.head())

# Define your date thresholds
train_end_date = '2021-03-31'
validation_end_date = '2021-04-30'

# Convert to datetime if not already
data['date'] = pd.to_datetime(data['date'])

# Split the data based on the date thresholds
train_data = data[data['date'] <= train_end_date]
validation_data = data[(data['date'] > train_end_date) & (data['date'] <= validation_end_date)]
test_data = data[data['date'] > validation_end_date]

# Check the dimensions of the datasets
print("Training dataset dimensions:", train_data.shape)
print("Validation dataset dimensions:", validation_data.shape)
print("Test dataset dimensions:", test_data.shape)
