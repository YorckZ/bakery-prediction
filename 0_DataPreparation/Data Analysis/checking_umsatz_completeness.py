import pandas as pd

# Load the provided CSV file
file_path = '../umsatzdaten_gekuerzt.csv'
data = pd.read_csv(file_path)

# Convert the date column to datetime type
data['Datum'] = pd.to_datetime(data['Datum'], errors='coerce')

# # Earliest and latest dates
earliest_date = data['Datum'].min()
latest_date = data['Datum'].max()

# Calculate the number of days between earliest and latest dates
days_between = (latest_date - earliest_date).days + 1

# Extract unique dates
unique_dates = data['Datum'].dt.normalize().unique()

# Sort the unique dates if needed
unique_dates_sorted = sorted(unique_dates)

# Count total entries and missing values
total_entries = len(unique_dates_sorted)
missing_entries = days_between - total_entries

# Coverage of data
coverage = round(len(unique_dates_sorted) / days_between * 100, 2)

print(f"Earliest Date: {earliest_date}")
print(f"Latest Date: {latest_date}")
print(f"Days Between Earliest and Latest Date: {days_between} days")
print("Anzahl von Tagen mit Umsätzen: ", len(unique_dates_sorted))
print(f"Total Number of Entries: {total_entries}")
print(f"Number of Missing Entries: {missing_entries}")
print(f"Data Coverage: {coverage} %")


# Get the unique values of 'Warengruppe' to iterate over them
# warengruppen = data['Warengruppe'].unique()
#
# Loop through each 'Warengruppe' and perform the calculations
# for gruppe in warengruppen:
#     # Filter the dataframe for the current 'Warengruppe'
#     filtered_data = data[data['Warengruppe'] == gruppe]
#
#     # Earliest and latest dates for the filtered data
#     earliest_date = filtered_data['Datum'].min()
#     latest_date = filtered_data['Datum'].max()
#
#     # Calculate the number of days between earliest and latest dates
#     days_between = (latest_date - earliest_date).days
#
#     # Count total entries and missing values for the filtered data
#     total_entries = len(filtered_data)
#     missing_entries = filtered_data['Datum'].isna().sum()
#
#     # Print the results for each 'Warengruppe'
#     print(f"Warengruppe: {gruppe}")
#     print(f"Earliest Date: {earliest_date}")
#     print(f"Latest Date: {latest_date}")
#     print(f"Days Between Earliest and Latest Date: {days_between} days")
#     print(f"Total Number of Entries: {total_entries}")
#     print(f"Number of Missing Entries: {missing_entries}")
#     print()
