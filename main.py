from pprint import pprint
import csv
import re


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


# with open("phonebook.csv", "w") as f:
#     datawriter = csv.writer(f, delimiter=',')
#     datawriter.writerows(contacts_list)

if __name__ == '__main__':
    read_csv("phonebook_raw.csv")
