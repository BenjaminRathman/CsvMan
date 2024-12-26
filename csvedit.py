import csv


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
    Filters rows by a column value and writes the entire row to a new CSV file.

    :param input_filepath: Path to the input CSV file.
    :param output_filepath: Path to the output CSV file.
    :param column_name: Name of the column to check.
    :param value: The value to look for in the specified column.
    """
    with open(input_filepath, 'r', newline='') as infile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames

        with open(output_filepath, 'w', newline='') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()

            for row in reader:
                if row.get(column_name) == value:
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









