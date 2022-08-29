def is_palindrome(string:str) -> bool:
    """
    Checks whether the given string is a palindrome.

    :param string: The string to check.
    :return: True if the string is a palindrome, False otherwise.
    """
    string = string.replace(" ","").lower()
    return string == string[::-1]
def run() -> None:
    """
    The main function of the program.
    """
    string:str = input("Enter the string to check: ")
    if is_palindrome(string):
        print(f"The {string} is a palindrome")
    else:
        print(f"The {string} is not a palindrome")

if __name__ == "__main__":
    run()