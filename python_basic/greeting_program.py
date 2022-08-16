from unicodedata import name


def run():
    user_name= input('Please enter your name: ')
    gretting = f'Hi {user_name} how are you  '
    print(gretting)
    print(f'Your  text string has {len(gretting)} characters.\n')
    print(f'Your  text string has {len(gretting.strip())} characters without spaces.\n')


if __name__ == '__main__':
    run()
