from datetime import datetime, timedelta
import pyperclip


def get_date_range():
    # Step 1: Ask for date input
    date_input = input("Enter a date range (e.g., 13.04.19-18.04.19): ").strip()
    try:
        start_str, end_str = date_input.split("-")

        # Parse the input dates
        start_date = datetime.strptime(start_str, "%d.%m.%y")
        end_date = datetime.strptime(end_str, "%d.%m.%y")

        # Check if the start date is before or equal to the end date
        if start_date > end_date:
            raise ValueError("Start date must be before or equal to the end date.")

        return start_date, end_date

    except ValueError as ve:
        print(f"Error: {ve}")
        return None, None


def generate_date_list(start_date, end_date):
    # Step 2: Create a list of all dates in the interval
    current_date = start_date
    date_list = []

    while current_date <= end_date:
        formatted_date = current_date.strftime("%Y-%m-%d")
        date_list.append(f"{formatted_date},1")
        current_date += timedelta(days=1)

    return date_list


def main():
    start_date, end_date = get_date_range()

    if start_date and end_date:
        # Generate the date list
        date_list = generate_date_list(start_date, end_date)

        # Step 3: Copy the list to clipboard
        output = "\n".join(date_list)
        pyperclip.copy(output)

        print("The following dates have been copied to the clipboard:")
        print(output)


if __name__ == "__main__":
    # Takes input such as "01.04.24-08.04.24" and copies to clipboard a list of all included dates in YYYY-MM-DD,1 format
    main()
