import pickle
import csv

def pickle_to_csv(pickle_file, csv_file):
    with open(pickle_file, 'rb') as f:
        data = pickle.load(f)

    keys = data[0].keys()

    with open(csv_file, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        for row in data:
            writer.writerow(row)

pickle_to_csv('package.pickle', 'package.csv')