import pandas as pd

# Load the provided CSV file
file_path = '../wetter.csv'
data = pd.read_csv(file_path)

# Extract unique elements from the last column ("Wettercode")
unique_elements = data['Wettercode'].dropna().unique()

# Convert to a sorted list for better readability
unique_elements_list = sorted(unique_elements)

# Convert the list of unique elements to integers
unique_elements_int_list = [int(element) for element in unique_elements_list]

print(unique_elements_int_list)
