def is_palindrome(string:str) -> bool:
    """
    Checks whether the given string is a palindrome.

    :param string: The string to check.
    :return: True if the string is a palindrome, False otherwise.
    """
    string = string.replace(" ","").lower()
    return string == string[::-1]
def run():
    """
    The main function of the program.
    """
    print("Enter the string to check.")
    string = input()
    if is_palindrome(string):
        print("The string is a palindrome")

if __name__ == "__main__":
    run()