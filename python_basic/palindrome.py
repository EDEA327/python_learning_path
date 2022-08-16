def palindrome(word):
    word = word.replace(' ', '')
    word = word.lower()
    inv_word = word[::-1]
    if word == inv_word:
        return True
    else:
        return False


def run():
    word = input('Write a word: ')
    is_palindrome = palindrome(word)
    if is_palindrome == True:
        print('Your word is a palindrome')
    else:
        print('Your word is not a palindrome')


if __name__ == '__main__':
    run()