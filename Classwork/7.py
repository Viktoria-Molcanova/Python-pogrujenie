import csv
import pickle


with open('file.csv', 'r') as file:
    csv_data = file.readlines()


pickle_data = pickle.dumps(csv_data)


print(pickle_data)