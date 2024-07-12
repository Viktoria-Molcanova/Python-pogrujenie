import os
import json
import csv
import pickle

def get_directory_info(directory):
    dir_info = {'name': os.path.basename(directory), 'type': 'directory', 'size': 0, 'children': []}

    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)

        if os.path.isfile(item_path):
            file_size = os.path.getsize(item_path)
            dir_info['size'] += file_size
            dir_info['children'].append({'name': item, 'type': 'file', 'size': file_size})
        elif os.path.isdir(item_path):
            sub_dir_info = get_directory_info(item_path)
            dir_info['size'] += sub_dir_info['size']
            dir_info['children'].append(sub_dir_info)

    return dir_info

def save_directory_info(directory, output_path):
    dir_info = get_directory_info(directory)

    with open(output_path + '.json', 'w') as json_file:
        json.dump(dir_info, json_file, indent=4)

    with open(output_path + '.csv', 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['name', 'type', 'size'])
        write_csv_rows(csv_writer, dir_info)

    with open(output_path + '.pickle', 'wb') as pickle_file:
        pickle.dump(dir_info, pickle_file)

def write_csv_rows(csv_writer, dir_info):
    for child in dir_info['children']:
        if child['type'] == 'file':
            csv_writer.writerow([child['name'], child['type'], child['size']])
        elif child['type'] == 'directory':
            csv_writer.writerow([child['name'], child['type'], child['size']])
            write_csv_rows(csv_writer, child)


directory_path = 'C:/Users/Виктория/Desktop/untitled/Homework'
output_path = 'C:/Users/Виктория/Desktop/untitled/Homework'
save_directory_info(directory_path, output_path)