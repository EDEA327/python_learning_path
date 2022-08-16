
def divide_elements_in_list(list,divider):
    try:
        return[i / divider for i in list]
    except ZeroDivisionError as e:
        return list

list = list(range(10))
divider = 2

print(divide_elements_in_list(list,divider))