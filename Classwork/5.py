import os
import json
import pickle

def convert_json_to_pickle(directory):
    for file in os.listdir(directory):
        if file.endswith(".json"):
            with open(os.path.join(directory, file), 'r', encoding='utf-8') as json_file:
                data = json.load(json_file)
                with open(os.path.join(directory, file.replace(".json", ".pickle")), 'wb') as pickle_file:
                    pickle.dump(data, pickle_file)
    print("Преобразование успешно завершено.")

directory_path = r"C:\Users\Виктория\Desktop\untitled\Classwork"
convert_json_to_pickle(directory_path)