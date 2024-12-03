# Folie 20
# Beispiel Vorhersage

import pandas as pd

# Create a new house with the following features
new_house = pd.DataFrame({
'sqft_lot15': [5000], # Square footage of lot
'condition': [3] # Overall condition of the house
})

# Use the model to predict the price of the new house
predicted_price = mod.predict(new_house)
print(f"The predicted price for the new house is: {predicted_price[0]}")
