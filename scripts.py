import csv
import json
from defusedxml import  ElementTree as ET
import os

def csv_operations():
    with open('data.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        data = [row for row in reader]

    new_entry = {'id': '3', 'name': 'Анна Аннова', 'email': 'anna@example.com'}
    data.append(new_entry)
    
    with open('csv_to_json.json', 'w') as jsonfile:
        json.dump(data, jsonfile, ensure_ascii=False, indent=2)

def xml_operations():
    tree = ET.parse('data.xml')
    root = tree.getroot()
    
    xml_dict = []
    for user in root.findall('user'):
        user_data = {
            'id': user.find('id').text,
            'name': user.find('name').text,
            'email': user.find('email').text
        }
        xml_dict.append(user_data)

    new_user = {'id': '3', 'name': 'Анна Аннова', 'email': 'anna@example.com'}
    xml_dict.append(new_user)
    
    with open('xml_to_csv.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['id', 'name', 'email'])
        writer.writeheader()
        writer.writerows(xml_dict)
    
    os.rename('xml_to_csv.csv', 'xml_to_csv.xml')


def json_operations():
    with open('data.json', 'r', encoding='utf-8') as jsonfile:
        data = json.load(jsonfile)
    
    tuple_data = tuple(tuple(item.values()) for item in data)
    
    new_data = {'id': 3, 'name': 'Анна Аннова', 'email': 'anna@example.com'}
    data.append(new_data)
    
    with open('json_to_csv.csv', 'w', newline='') as csvfile:
        fieldnames = data[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(data)

try:
    csv_operations()
    xml_operations()
    json_operations()
except Exception as e:
    print(f"Ошибка при обработке файлов: {str(e)}")