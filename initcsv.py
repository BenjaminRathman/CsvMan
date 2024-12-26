import csv
import os 


class Csv:
    def __init__(self, name, filepath=None):
        self.name = name
        
        # Handle empty filepath with valid name - create new file
        if filepath is None and name:
            # Create filepath using current directory and name
            self.filepath = os.path.join(os.getcwd(), f"{name}.csv")
            # Create empty CSV file
            with open(self.filepath, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([])  # Write empty row to initialize file
            print(f"Created new CSV file: {self.filepath}")
            
        # Handle invalid filepath
        elif filepath and not os.path.exists(filepath):
            raise FileNotFoundError(f"The file path does not exist: {filepath}")
            
        # Valid filepath provided
        else:
            self.filepath = filepath



        

