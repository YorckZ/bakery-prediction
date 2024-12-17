import pandas as pd
import matplotlib.pyplot as plt


def filter_data(ware_id):
    # Load the provided CSV file
    umsatzdaten_file = '../umsatzdaten_gekuerzt.csv'
    umsatz_data = pd.read_csv(umsatzdaten_file)

    # Convert to datetime if not already
    umsatz_data['Datum'] = pd.to_datetime(umsatz_data['Datum'])

    # Drop everything except for seasonal products
    data = umsatz_data[umsatz_data['Warengruppe'] == ware_id]

    # Now drop column Warengruppe, as we have already filtered successfully
    data = data.drop(columns=['Warengruppe'])

    # Ensure the data is sorted by date
    data = data.sort_values(by='Datum')

    # Save the filtered data as file
    # filtered_data.to_csv('filtered_data.csv', index=False)
    return data


def get_monthly_statistics(data):
    """
    Prints the number of entries and total Umsatz per month for the dataset.

    Parameters:
    data (DataFrame): Pandas DataFrame with 'Datum' and 'Umsatz' columns.
    """
    # Ensure 'Datum' is in datetime format
    data['Datum'] = pd.to_datetime(data['Datum'])

    # Extract year and month as a combined column
    data['YearMonth'] = data['Datum'].dt.to_period('M')

    # Group by YearMonth and calculate statistics
    monthly_stats = data.groupby('YearMonth').agg(
        Entries=('Datum', 'count'),
        TotalUmsatz=('Umsatz', 'sum')
    )

    return monthly_stats


def print_monthly_stats(monthly_stats):
    # Print the results
    for period, row in monthly_stats.iterrows():
        print(f"{period}: Entries = {row['Entries']}, Total Umsatz = {row['TotalUmsatz']:.2f}")


def plot_monthly_statistics(data):
    """
    Generates a bar diagram showing months on the x-axis and Total Umsatz on the y-axis.
    Each bar includes descriptions with number of entries and Total Umsatz.
    Adds a red horizontal line indicating the global average of Total Umsatz.

    Parameters:
    data (DataFrame): Pandas DataFrame with 'Datum' and 'Umsatz' columns.
    """
    # Ensure 'Datum' is in datetime format
    data['Datum'] = pd.to_datetime(data['Datum'])

    # Extract year and month as a combined column
    data['YearMonth'] = data['Datum'].dt.to_period('M')

    # Group by YearMonth and calculate statistics
    monthly_stats = data.groupby('YearMonth').agg(
        Entries=('Datum', 'count'),
        TotalUmsatz=('Umsatz', 'sum')
    ).reset_index()

    # Calculate the global average of Total Umsatz
    global_average = monthly_stats['TotalUmsatz'].mean()

    # Convert YearMonth to string for x-axis
    monthly_stats['YearMonth'] = monthly_stats['YearMonth'].astype(str)

    # Plotting the bar chart
    fig, ax = plt.subplots(figsize=(12, 6))
    bars = ax.bar(monthly_stats['YearMonth'], monthly_stats['TotalUmsatz'], color='skyblue')

    # Adding annotations to each bar
    for bar, entries, total_umsatz in zip(bars, monthly_stats['Entries'], monthly_stats['TotalUmsatz']):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 50,
            f'{entries} entries\n{total_umsatz:.2f} €',
            ha='center',
            va='bottom',
            fontsize=10
        )

    # Adding a red horizontal line for the global average
    ax.axhline(global_average, color='red', linestyle='--', linewidth=1.5,
               label=f'Global Average: {global_average:.2f} €')

    # Adding a legend
    ax.legend(fontsize=10)

    # Setting labels and title
    ax.set_xlabel('Month', fontsize=12)
    ax.set_ylabel('Total Umsatz (€)', fontsize=12)
    ax.set_title('Monthly Total Umsatz and Number of Entries (with Global Average)', fontsize=14)
    plt.xticks(rotation=45, fontsize=10)

    plt.tight_layout()
    plt.show()


def analyze_sales(wid):
    filtered_data = filter_data(wid)
    stats = get_monthly_statistics(filtered_data)
    # print_monthly_stats(stats)
    plot_monthly_statistics(filtered_data)


def plot_total_umsatz_by_warengruppe():
    """
    Generates a line diagram showing the total Umsatz per month for each Warengruppe.

    Parameters:
    data (DataFrame): Pandas DataFrame with 'Datum', 'Umsatz', and 'Warengruppe' columns.
    """
    # Load the provided CSV file
    umsatzdaten_file = '../umsatzdaten_gekuerzt.csv'
    data = pd.read_csv(umsatzdaten_file)

    # Ensure 'Datum' is in datetime format
    data['Datum'] = pd.to_datetime(data['Datum'])

    # Extract year and month as a combined column
    data['YearMonth'] = data['Datum'].dt.to_period('M')

    # Group by YearMonth and Warengruppe to calculate total Umsatz
    monthly_stats = data.groupby(['YearMonth', 'Warengruppe'])['Umsatz'].sum().reset_index()

    # Pivot table for easier plotting
    pivot_table = monthly_stats.pivot(index='YearMonth', columns='Warengruppe', values='Umsatz')

    # Plotting the line diagram
    fig, ax = plt.subplots(figsize=(14, 7))
    pivot_table.plot(ax=ax, marker='o')

    # Setting labels and title
    ax.set_xlabel('Month', fontsize=12)
    ax.set_ylabel('Total Umsatz (€)', fontsize=12)
    ax.set_title('Total Umsatz per Month for Each Warengruppe', fontsize=14)
    ax.legend(title='Warengruppe', fontsize=10, title_fontsize=12)
    plt.xticks(rotation=45, fontsize=10)
    plt.grid(axis='y', linestyle='--', linewidth=0.5)

    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    # Analyze sales ware waregroup id
    # analyze_sales(1)

    # Analyze all sales
    plot_total_umsatz_by_warengruppe()
