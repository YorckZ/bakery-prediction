import pandas as pd

# Load the CSV files into pandas DataFrames
umsatzdaten = pd.read_csv("umsatzdaten_gekuerzt.csv")
# print(umsatzdaten.shape)

# Feiertage
feiertage = pd.read_csv("Feiertag.csv")
merged_data = umsatzdaten.merge(feiertage, on='Datum', how='left')
merged_data['Feiertag'].fillna(0, inplace=True)
# print(merged_data.shape)

# Kieler Woche
ki_wo = pd.read_csv("kiwo.csv")
merged_data = merged_data.merge(ki_wo, on='Datum', how='left')
merged_data['KielerWoche'].fillna(0, inplace=True)
# print(merged_data.shape)

# Public Viewing
public_viewing = pd.read_csv("PublicViewing.csv")
merged_data = merged_data.merge(public_viewing, on='Datum', how='left')
merged_data['PublicViewing'].fillna(0, inplace=True)
# print(merged_data.shape)

# Schulferien
schulferien = pd.read_csv("Schulferien.csv")
merged_data = merged_data.merge(schulferien, on='Datum', how='left')
merged_data['Schulferien'].fillna(0, inplace=True)
# print(merged_data.shape)

# Warengruppenlabel
warengruppenlabel = pd.read_csv("Warengruppenlabel.csv")
merged_data = umsatzdaten.merge(warengruppenlabel, left_on='Warengruppe', right_on='ID', how='left')
# print(merged_data.shape)

# Wetter
# TODO: Fill blanks?
wetter = pd.read_csv("wetter.csv")
merged_data = merged_data.merge(wetter, on='Datum', how='left')
# merged_data['Schulferien'].fillna(0, inplace=True)
# Bewoelkung,Temperatur,Windgeschwindigkeit,Wettercode
# print(merged_data.shape)

# Wettercodes
# TODO: Are there any blanks?
wettercodes = pd.read_csv("wettercodes.csv")
merged_data = merged_data.merge(wettercodes, on='Wettercode', how='left')
# merged_data['Schulferien'].fillna(0, inplace=True)
# Bewoelkung,Temperatur,Windgeschwindigkeit,Wettercode
# print(merged_data.shape)

# Transform column 'Datum' into a datetime object
merged_data['Datum'] = pd.to_datetime(merged_data['Datum'], format='%Y-%m-%d')

# Add a new column 'Wochentag' with the weekday calculated from 'Datum'
merged_data['Wochentag'] = merged_data['Datum'].dt.day_name()

# Add a new column 'Monat' with the month calculated from 'Datum'
merged_data['Monat'] = merged_data['Datum'].dt.month_name()

# Add one-hot encoding for the 'Wochentag' column
wochentag_one_hot = pd.get_dummies(merged_data['Wochentag'], prefix='Wochentag')
merged_data = pd.concat([merged_data, wochentag_one_hot], axis=1)

# Add one-hot encoding for the 'Monat' column
monat_one_hot = pd.get_dummies(merged_data['Monat'], prefix='Monat')
merged_data = pd.concat([merged_data, monat_one_hot], axis=1)

# Drop the 'Wochentag' and 'Monat' columns
merged_data.drop(columns=['Wochentag', 'Monat'], inplace=True)

# Display the merged DataFrame
print(merged_data.shape)
print(merged_data.columns)
# print(merged_data.head())
# print(merged_data)

# Optionally save the merged DataFrame to a new CSV file
# merged_data.to_csv("merged_umsatzdaten.csv", index=False)
