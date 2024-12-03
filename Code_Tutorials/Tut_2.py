# Folie 18
# Beispiel Datensatzteilung (keine Zeitreihe)

import pandas as pd
from sklearn.model_selection import train_test_split

# Load the dataset
# url = "https://raw.githubusercontent.com/opencampus-sh/einfuehrung-in-data-science-undml/main/house_pricing_data/house_pricing_train.csv"
url = "house_pricing_train.csv"
data = pd.read_csv(url)

# Set a random seed for reproducibility
random_state = 42

# First, split the data into training (70%) and remaining (30%)
train_data, remaining_data = train_test_split(data, train_size=0.7, random_state=random_state)

# Now split the remaining data into validation (2/3 of remaining) and test (1/3 of remaining)
validation_data, test_data = train_test_split(remaining_data, test_size=0.3333, random_state=random_state)

# Check the dimensions of the datasets
print("Training dataset dimensions:", train_data.shape)
print("Validation dataset dimensions:", validation_data.shape)
print("Test dataset dimensions:", test_data.shape)
