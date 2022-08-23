
def quit_repeated(my_list):
    my_list = list(set(my_list))
    return my_list


def run():
    elements_length = int(input(" How many elements? : "))
    if elements_length <= 0 :
        raise ValueError("You must provide at least one element")
    elements = [input(f" Type your {i} element for the  list: ") for i in range(1,elements_length+1)]
    print("Original list = ",elements)
    print(f"List without repeated elements:{quit_repeated(elements)} ")
if __name__ == '__main__':
    run()