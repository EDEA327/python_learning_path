def run():
    square = [i**2 for i in range(1,101) if i % 3 != 0]
    print(square)
    # Challenge list
    list_4_9_6 = [i for i in range(1,10000) if i % 36 == 0 ]
    print(list_4_9_6)
if  __name__ == '__main__':
    run()