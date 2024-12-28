import csv
from datetime import datetime


def extract_single_column(input_filepath, output_filepath, column_name):
    """
    Extracts a single column from a CSV file and writes it to a new CSV file.

    :param input_filepath: Path to the input CSV file.
    :param output_filepath: Path to the output CSV file.
    :param column_name: Name of the column to extract.
    """
    with open(input_filepath, 'r', newline='') as infile:
        reader = csv.DictReader(infile)

        with open(output_filepath, 'w', newline='') as outfile:
            fieldnames = [column_name]
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()

            for row in reader:
                if column_name in row:
                    writer.writerow({column_name: row[column_name]})



'''This function takes in 2 files and a column name and a value if the value is found in that column it will read and write all the data in that row '''

def filter_rows_by_column(input_filepath, output_filepath, column_name, value):
    """
    Filters rows by a column value and writes the matching rows to a new CSV file.

    :param input_filepath: Path to the input CSV file.
    :param output_filepath: Path to the output CSV file.
    :param column_name: Name of the column to check.
    :param value: The value to look for in the specified column.
    """
    with open(input_filepath, 'r', newline='', encoding='utf-8') as infile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames

        if not fieldnames:
            raise ValueError("Input file is empty or invalid CSV format.")

        with open(output_filepath, 'w', newline='', encoding='utf-8') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()

            for row in reader:
                # Compare the column value directly for exact matches
                if row.get(column_name) == str(value):  # Ensure both are strings
                    writer.writerow(row)
                    

'''this is code that finds a value in a column and replaces it with a given value'''
def replace_value_in_column(input_filepath, output_filepath, column_name, old_value, new_value):
    """
    Replaces a specific value in a column with a new value and writes the updated rows to a new CSV file.

    :param input_filepath: Path to the input CSV file.
    :param output_filepath: Path to the output CSV file.
    :param column_name: Name of the column to check.
    :param old_value: The value to be replaced.
    :param new_value: The new value to replace the old value.
    """
    with open(input_filepath, 'r', newline='') as infile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames

        with open(output_filepath, 'w', newline='') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()

            for row in reader:
                if row.get(column_name) == old_value:
                    row[column_name] = new_value
                writer.writerow(row)




'''this based off of a column sorts based on time'''
def sort_csv_by_time(input_filepath, output_filepath, time_column, time_format):
    """
    Sorts the rows in a CSV file by the specified time column and writes the sorted rows to a new CSV file.

    :param input_filepath: Path to the input CSV file.
    :param output_filepath: Path to the output CSV file.
    :param time_column: Name of the column containing time data.
    :param time_format: Format of the time data in the column (e.g., "%H:%M", "%Y-%m-%d %H:%M").
    """
    with open(input_filepath, 'r', newline='', encoding='utf-8') as infile:
        reader = csv.DictReader(infile)
        rows = list(reader)

        # Sort rows by the time column
        try:
            sorted_rows = sorted(
                rows,
                key=lambda row: datetime.strptime(row[time_column], time_format)
            )
        except ValueError as e:
            raise ValueError(f"Error parsing time values: {e}")

        fieldnames = reader.fieldnames

    # Write the sorted rows to the output file
    with open(output_filepath, 'w', newline='', encoding='utf-8') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(sorted_rows)

    print(f"CSV sorted by '{time_column}' and saved to: {output_filepath}")




def filter_rows_by_multiple_values(input_filepath, output_filepath, column_name, values_list):
    """
    Filters rows by multiple values in a specified column and writes matching rows to a new CSV file.

    :param input_filepath: Path to the input CSV file.
    :param output_filepath: Path to the output CSV file.
    :param column_name: Name of the column to check.
    :param values_list: List of values to match in the specified column.
    """
    with open(input_filepath, 'r', newline='', encoding='utf-8') as infile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames

        if not fieldnames:
            raise ValueError("Input file is empty or invalid CSV format.")

        with open(output_filepath, 'w', newline='', encoding='utf-8') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()

            for row in reader:
                # Check if the column value is in the list of values
                if row.get(column_name) in values_list:
                    writer.writerow(row)

    print(f"Filtered data saved to: {output_filepath}")

