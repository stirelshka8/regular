from pprint import pprint
import csv
import re


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
    print(patedited)

    with open(file_names, 'w+', encoding='utf8') as rec_files:
        rec_files.write(patedited)


# with open("phonebook.csv", "w") as f:
#     datawriter = csv.writer(f, delimiter=',')
#     datawriter.writerows(contacts_list)

if __name__ == '__main__':
    file_name = "phonebook_raw.csv"
    editing_phone_number(file_name)
    # pprint(read_csv(file_name))
