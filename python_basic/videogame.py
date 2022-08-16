import random
def run():
    random_num = random.randint(1,100)
    user_num= int(input("Type a numer from 1 to 100: "))
    while user_num != random_num:
        if user_num < random_num:
            print('Type a bigger number')
        else:
            print('Type a smaller number')
        user_num= int(input("Type another number from 1 to 100: "))
    print('You Win!!!')

if __name__ == '__main__':
    run()