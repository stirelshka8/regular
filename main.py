from pprint import pprint
import csv


def read_csv(filename):
    with open(filename) as read_file:
        rows = csv.reader(read_file, delimiter=",")
        contacts_list = list(rows)
        pprint(contacts_list)


# with open("phonebook.csv", "w") as f:
#     datawriter = csv.writer(f, delimiter=',')
#     datawriter.writerows(contacts_list)

if __name__ == '__main__':
    read_csv("phonebook_raw.csv")
