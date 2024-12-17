import csv
from datetime import datetime


def predict_sales(date, value):
    # Creates a sample sales prediction by pure chance. Technical proof-of-concept
    return round(float(hash(date) % 10000) * value / 100, 2)


input_file = '../0_DataPreparation/sample_submission.csv'
output_file = 'output.csv'


# Input file, output file
with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    # Write header
    header = next(reader)
    writer.writerow(header)

    # Process each row
    for row in reader:
        id_value = row[0]
        date_part = id_value[:6]  # Extracting the date part (first 6 characters)
        product = id_value[6:]  # Extracting the product part (last character)

        # Formatting date
        try:
            formatted_date = datetime.strptime(date_part, '%y%m%d').strftime('%Y-%m-%d')
        except ValueError:
            print(f"Invalid date format in ID {id_value}. Skipping row.")
            continue

        # Predicting sales
        predicted_value = predict_sales(formatted_date, int(product))

        # Updating the row and writing to output
        row[1] = predicted_value
        writer.writerow(row)
