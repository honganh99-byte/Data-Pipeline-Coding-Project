import csv
import os
def load_data(data, output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open (output_path, "w") as outfile:
        writer = csv.DictWriter(outfile,fieldnames=data[0].keys())
        #write this csv file using these columns, give one dict per row
        writer.writeheader()
        #writer is a variable assigned from DictWriter
        writer.writerows(data)
