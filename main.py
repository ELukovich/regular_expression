from pprint import pprint

import csv

import re

## Читаем адресную книгу в формате CSV в список contacts_list:
with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
    #pprint(contacts_list)

## 1. Выполните пункты 1-3 задания.
def name_normal(rows):
    result = [' '.join(employee[0:3]).split(' ')[0:3] + employee[3:7] for employee in rows]

    return result

def remove_duplicat(correct_name_list):
    no_duplicat = []
    for compared in correct_name_list:
        for employee in correct_name_list:
            if compared[0:2] == employee[0:2]:
                list_employee = compared
                compared = list_employee[0:2]
                for i in range(2, 7):
                    if list_employee[i] == '':
                        compared.append(employee[i])
                    else:
                        compared.append(list_employee[i])
        if compared not in no_duplicat:
            no_duplicat.append(compared)

    return no_duplicat

def updating_phone_numbers(rows, phones, new):
    phonebook = []
    pattern = re.compile(phones)
    phonebook = [[pattern.sub(new, string) for string in strings] for strings in rows]

    return phonebook

correct_name_list = name_normal(contacts_list)
no_duplicates_list = remove_duplicat(correct_name_list)
phones = r'(\+7|8)+[\s(]*(\d{3,3})[\s)-]*(\d{3})[\s-]*(\d{2})[\s-]*(\d{2})'
correct_phones = updating_phone_numbers(no_duplicates_list, phones, r'+7(\2)\3-\4-\5')
phones_dob = r'(\+7|8)+[\s(]*(\d{3,3})[\s)-]*(\d{3})[\s-]*(\d{2})[\s-]*(\d{2})[\s]*[(доб.\s]*(\d+)[)]*'
correct_phonebook = updating_phone_numbers(correct_phones, phones_dob, r'+7(\2)\3-\4-\5 доб.\6')

## 2. Сохраните получившиеся данные в другой файл.
with open("phonebook.csv", "w", encoding='utf-8') as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(correct_phonebook)