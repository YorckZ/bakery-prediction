import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


def create_dataframe():
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
    return merged_df


def create_model():
    # Create a pipeline to handle preprocessing and regression
    pipeline = Pipeline(steps=[('scaler', StandardScaler()), ('regressor', LinearRegression())])
    return pipeline


def split_data(df, sd):
    # Split the data based on the date thresholds
    train_data = df[df['Datum'] <= sd]
    validation_data = df[(df['Datum'] > sd)]
    return train_data, validation_data


def train_model(m, t):
    # Select features and target variable
    x = t[['Temperatur', 'Windgeschwindigkeit']]  # Features
    y = t['Umsatz']  # Target

    # Train the model
    m.fit(x, y)
    return m


def predict(m, v):
    """

    :param m: The model used for prediction
    :param v: The validation dataset
    :return: The set of predicted values
    """
    # Select features for validation
    x_val = v[['Temperatur', 'Windgeschwindigkeit']]  # Features

    # Make predictions
    predictions = m.predict(x_val)
    return predictions


def evaluate_model(m, v, p):
    """

    :param m: The model being evaluated
    :param v: The validation dataset
    :param p: The predicted values
    :return: None
    """
    # Select target variable for validation
    y_val = v['Umsatz']  # Actual target values

    # Evaluate the model
    mse = mean_squared_error(y_val, p)
    r2 = r2_score(y_val, p)

    # Print evaluation metrics
    print("Model Coefficients:", m.named_steps['regressor'].coef_)
    print("Model Intercept:", m.named_steps['regressor'].intercept_)
    print("Mean Squared Error:", mse)
    print("R-squared:", r2)


if __name__ == "__main__":
    # This is an attempt at a clean master codebase for everyone to work on
    dataframe = create_dataframe()
    model = create_model()
    split_date = '2017-07-31'
    training, validation = split_data(dataframe, split_date)
    trained_model = train_model(model, training)
    prediction = predict(model, validation)
    evaluate_model(model, validation, prediction)
