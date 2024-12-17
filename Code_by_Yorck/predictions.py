import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


def create_training_set():
    # Load data
    umsatzdaten_file = '../0_DataPreparation/umsatzdaten_gekuerzt.csv'

    # Convert data to pandas dataframes
    umsatzdaten_df = pd.read_csv(umsatzdaten_file)

    # Return dataframe
    return umsatzdaten_df


def load_prediction_set():
    # Load data
    prediction_file = '../0_DataPreparation/sample_submission.csv'

    # Convert data to pandas dataframes
    prediction_df = pd.read_csv(prediction_file)

    # Return dataframe
    return prediction_df


def enrich_dataset(data):
    # Load data
    wetter_file = '../0_DataPreparation/wetter.csv'
    kiwo_file = '../0_DataPreparation/kiwo.csv'
    feiertag_file = '../0_DataPreparation/Feiertag.csv'
    pubview_file = '../0_DataPreparation/PublicViewing.csv'
    # ferien_file = '../0_DataPreparation/Schulferien.csv'
    # wettercodes_file = '../0_DataPreparation/wettercodes.csv'

    # Convert data to pandas dataframes
    wetter_df = pd.read_csv(wetter_file)
    kiwo_df = pd.read_csv(kiwo_file)
    feiertag_df = pd.read_csv(feiertag_file)
    pubview_df = pd.read_csv(pubview_file)
    # ferien_df = pd.read_csv(ferien_file)
    # wettercodes_df = pd.read_csv(wettercodes_file)

    # Merge dataframes via inner join on 'Datum'
    # merged_df = data
    merged_df = pd.merge(data, wetter_df, on='Datum', how='left')
    merged_df = pd.merge(merged_df, kiwo_df, on='Datum', how='left')
    # merged_df = pd.merge(merged_df, feiertag_df, on='Datum', how='left')
    # merged_df = pd.merge(merged_df, pubview_df, on='Datum', how='left')
    # ...

    # Drop rows with missing values
    merged_df = merged_df.dropna()

    # Convert to datetime if not already
    merged_df['Datum'] = pd.to_datetime(merged_df['Datum'])

    # Ensure the data is sorted by date
    merged_df = merged_df.sort_values(by='Datum')

    # Add additional features
    # ...

    return merged_df


def create_model():
    # Create a pipeline to handle preprocessing and regression
    pipeline = Pipeline(steps=[('scaler', StandardScaler()), ('regressor', LinearRegression())])
    return pipeline


def train_model(m, t):
    # Select features and target variable
    x = t[['Temperatur', 'Windgeschwindigkeit']]  # Features
    y = t['Umsatz']  # Target

    # Train the model
    m.fit(x, y)
    return m


if __name__ == '__main__':
    # This is an attempt at a clean master codebase with an enriched database for everyone to work on.
    # Splits data into training, validation, and testing.

    # Umsatzdaten
    ud = create_training_set()
    ud = enrich_dataset(ud)

    # Prediction Data
    # pd = load_prediction_set()
    # pd = enrich_dataset(pd)

    # model = create_model()
    # trained_model = train_model(model, ud)

    # Todo: create and output predictions

    print(ud)
