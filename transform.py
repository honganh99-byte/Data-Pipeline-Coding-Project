from extract import extract_data
from datetime import datetime
def transform_data(data):
    transformed = []
    for row in data:
        quantity = int(row["quantity"])
        price = float(row["price"])
        total = round(quantity * price, 2)

        new_date = datetime.strptime(row["date"], "%Y-%m-%d").strftime("%d-%b-%Y")
                            #parse, format
        row["total"] = total
        row["date"] = new_date

        transformed.append(row)

    return transformed

