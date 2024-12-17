import csv
from datetime import datetime


input_file = 'sample_submission.csv'


# Input file, output file
with open(input_file, 'r') as infile:
    reader = csv.reader(infile)

    # Write header
    header = next(reader)

    dates = {}

    # Process each row
    for row in reader:
        id_value = row[0]
        date_part = id_value[:6]  # Extracting the date part (first 6 characters)
        product = id_value[6:]  # Extracting the product part (last character)

        # Formatting date
        try:
            formatted_date = datetime.strptime(date_part, '%y%m%d').strftime('%Y-%m-%d')
            dates[formatted_date] = 0
        except ValueError:
            print(f"Invalid date format in ID {id_value}. Skipping row.")
            continue

    # Counts how many elements need to be predicted.
    print(len(dates))
