import csv

from funcs import fullName, union, correct_phone

with open("adress_book.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    list_1 = list(rows).copy()
    contacts_list = [list_1[0]]
    for item in list(map(fullName, list(list_1)[1:])):
        contacts_list.append(item)


ideal_dict = {contacts_list[0][0]: contacts_list[0][1:]}
for item in contacts_list[1:]:
    if item[0] not in ideal_dict:
        ideal_dict[item[0]] = item[1:]
    else:
        ideal_dict[item[0]] = union(ideal_dict[item[0]], item[1:])


ideal_list = [[key] + val for key, val in ideal_dict.items()]
new_ideal_list = list(map(correct_phone, ideal_list))

if __name__ == '__main__':
    with open("phonebook.csv", "w", encoding='utf-8') as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(new_ideal_list)








