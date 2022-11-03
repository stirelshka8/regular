from pprint import pprint
import csv


with open("phonebook_raw.csv") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
    pprint(contacts_list)





















# with open("phonebook.csv", "w") as f:
#     datawriter = csv.writer(f, delimiter=',')
#     datawriter.writerows(contacts_list)