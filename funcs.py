import re
def fullName(list_1):
    list_1.remove('')
    pop_ = []
    if list_1[0].count(' ') == 1:
        pop_ = list_1.pop(0).split()

    elif list_1[1].count(' ') == 1:
        return list_1[0].split() + list_1[1].split() + list(list_1[2:])

    elif list_1[0].count(' ') == 2:
        pop_ = list_1.pop(0).split()
        list_1.remove('')


    pop_.extend(list_1)
    return pop_

def union(list_1, list_2):
    list_3 = []
    for index in range(len(list_1)):
        if list_1[index] != '' or (list_1[index] == '' and list_2[index] == ''):
            list_3.append(list_1[index])
        elif list_2[index] != '':
            list_3.append(list_2[index])
        # elif :
        #     list_3.append(list_1[index])
    return list_3

def correct_phone(list_):
    if '(' in list_[5]:
        list_[5] = list_[5].replace('(', '')
    if ')' in list_[5]:
        list_[5] = list_[5].replace(')', '')

    pattern_1 = r"(\+7|8)\s?(\d+)[\s|-]?(\d{3})-?(\d{2})-?(\d{2})\s?(\([а-я]{3}\.\s\d+\)|[а-я]{3}\.\s\d+)?"
    if 'доб' not in list_[5]:
        sub_1 = r'+7(\2)\3-\4-\5'
        list_[5] = re.sub(pattern_1, sub_1, list_[5])
        return list_

    sub_2 = r'+7(\2)\3-\4-\5 (\6)'
    list_[5] = re.sub(pattern_1, sub_2, list_[5])
    return list_