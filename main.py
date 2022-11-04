import itertools
import operator
from pprint import pprint
import csv
import re

file_name = "phonebook_raw.csv"


# Функция считывания файла и первоначальной обработки
def read_csv(filename):
    dict_contact = []
    with open(filename) as read_file:
        rows = csv.reader(read_file, delimiter=",")
        contacts_list = list(rows)
        # pprint(contacts_list[0])

        # Переменная хранит в себе имена полей
        dict_key = contacts_list[0]
        # Переменная хранит в себе данные таблицы
        dict_val = contacts_list[1:]

        # Извлекаем данные, попутно нумеруя
        for data_key, data_val in enumerate(dict_val):
            dict_contact.append({})
            # print(data_key)
            # print(data_val)
            # Формируем словарь
            for format_key, format_val in zip(dict_key, data_val):
                # pprint(format_key)
                # pprint(format_val)
                dict_contact[data_key].update({format_key: format_val})

    # print(dict_contact[0])
    return dict_contact


# Функция правки номеров телефонов
def editing_phone_number(file_names):
    with open(file_names, encoding='utf8') as open_file:
        read_file = open_file.read()

    patphone = r'(\+7|8)?\s*\(?(\d{3})\)?[\s*-]?(\d{3})[\s*-]?(\d{2})[\s*-]?(\d{2})(\s*)\(?(доб\.?)?\s*(\d*)?\)?'
    patedited = re.sub(patphone, r'+7(\2)\3-\4-\5\6\7\8', read_file)
    # print(patedited)

    with open(file_names, 'w+', encoding='utf8') as rec_files:
        rec_files.write(patedited)


# Функция правки ФИО
def editing_name(file_names):
    dict_edit_name = read_csv(file_names)
    for data_edname in dict_edit_name:
        spdata = data_edname['lastname'].split(' ')
        # print(spdata)
        if len(spdata) > 1:
            data_edname['lastname'] = spdata[0]
            data_edname['firstname'] = spdata[1]
            if len(spdata) > 2:
                data_edname['surname'] = spdata[2]

        spdata = data_edname['firstname'].split(' ')
        # print(spdata)
        if len(spdata) > 1:
            data_edname['firstname'] = spdata[0]
            data_edname['surname'] = spdata[1]

    # print(dict_edit_name)
    return dict_edit_name


def unite(ednames):
    key_ = set(ednames[0].keys())
    list_ = ['firstname', 'lastname']
    llist_ = operator.itemgetter(*list_)
    column_ = operator.itemgetter(*(key_ ^ set(list_)))
    ednames.sort(key=llist_)
    group = itertools.groupby(ednames, llist_)
    # print(group)

    dict_ = []

    for (firstname, lastname), groups in group:
        dict_.append({'lastname': lastname, 'firstname': firstname})
        for grgroup in groups:
            didict = dict_[-1]
            for key, val in grgroup.items():
                if key not in didict or didict[key] == '':
                    didict[key] = val
    # print(dict_)
    return dict_


def write_to_file(filenames, dictos):
    key = list(dictos[0].keys())
    # print(key)
    with open(filenames, 'w', encoding='utf8') as file:
        write = csv.writer(file, delimiter=',')
        write.writerow(key)
        for dididictos in dictos:
            write.writerow(dididictos.values())


if __name__ == '__main__':
    editing_phone_number(file_name)
    edname = editing_name(file_name)
    unites = unite(edname)
    write_to_file("phonebook.csv", unites)
