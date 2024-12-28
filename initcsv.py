import csv
import os
import pandas as pd  # type: ignore

class CsvFile:
    def __init__(self, name):
        self.name = name
        self.filepath = self._ensure_file_exists(name)

    def _ensure_file_exists(self, name):
        """
        Check if the file exists in the folder. Depending on the file type:
        - If it's an Excel file (.xls/.xlsx), convert it to CSV.
        - If it's a CSV file, just attach its file path.
        - If it doesn't exist, create an empty CSV file with that name.
        """
        for extension in ['.csv', '.xls', '.xlsx']:
            potential_path = os.path.join(os.getcwd(), f"{name}{extension}")
            if os.path.exists(potential_path):
                if extension in ['.xls', '.xlsx']:
                    csv_path = os.path.join(os.getcwd(), f"{name}.csv")
                    self._excel_to_csv(potential_path, csv_path)
                    print(f"Converted Excel file to CSV: {csv_path}")
                    return csv_path
                elif extension == '.csv':
                    print(f"CSV file found: {potential_path}")
                    return potential_path

        # If no file exists, create a new CSV file
        csv_path = os.path.join(os.getcwd(), f"{name}.csv")
        with open(csv_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([])  # Initialize with an empty row
        print(f"Created new CSV file: {csv_path}")
        return csv_path

    @staticmethod
    def _excel_to_csv(input_excel_filepath, output_csv_filepath):
        """Convert an Excel file to a CSV file."""
        df = pd.read_excel(input_excel_filepath)
        df.to_csv(output_csv_filepath, index=False)



        

