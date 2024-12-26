import initcsv


def create(name):
    return initcsv.Csv(name)  # Return the Csv instance


def main(lst_of_csv):
    csv_dict = {}  # Initialize an empty dictionary
    for name in lst_of_csv:
        csv_instance = create(name)  # Create the Csv instance
        csv_dict[csv_instance.name] = csv_instance  # Use the name attribute from the instance
        


