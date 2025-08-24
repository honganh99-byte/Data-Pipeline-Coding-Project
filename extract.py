import csv
import os


def extract_data(csv_path):
    if not os.path.exists(csv_path):
        raise FileNotFoundError("Input file not found")

    with open(csv_path, "r") as file:
        reader = csv.DictReader(file)
        data = list(reader)

    return data 




