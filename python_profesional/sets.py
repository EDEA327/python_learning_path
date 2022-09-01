from typing import Any,List

def remove__duplicates(my_list:List[Any]) -> List[Any]:
    """
    Remove duplicates from a list.
    """
    return list(set(my_list))
def run():
    n_elements:int = int(input("Number of elements: "))
    assert n_elements > 0 , "Number of elements must be positive integer"
    my_list: List[Any] = [input(f"Type the {i} value of the list: ") for i in range(n_elements)]
    without_duplicates: List[Any] = remove__duplicates(my_list)
    print(f"The list whitout duplicates is {without_duplicates}")
if __name__ == '__main__':
    run()