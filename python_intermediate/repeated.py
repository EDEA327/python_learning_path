
def quit_repeated(my_list):
    my_list = list(set(my_list))
    return my_list


def run():
    elements = []
    elements_length = input(" How many elements? : ")
    assert elements_length.isnumeric(),"Given number of elements must be a number"
    if int(elements_length) <= 0:
        raise ValueError("You must provide at least one element")

    for i in range(1,elements_length+1):
        element = input(f" Type your {i} element for the  list: ")
        elements.append(element)

    print("elements = ",elements)
    print(f"elements without repeated elements:{quit_repeated(elements)} ")
if __name__ == '__main__':
    run()