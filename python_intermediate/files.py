
#! Global variables
names = []
#* Functions to be used
def read():
    """_This function allows you to read a file and do some more things to be useful_
    """
    with open("./files/name.txt", "r", encoding="utf-8") as f:
        for line in f:
            if len(line.strip()) > 0:
                names.append(line.strip())
    if len(names)> 0:
        print(names)
    else:
        print("Empty file")

def write():
    """_This function allows you to write a file and do some more things to be useful_
    """
    with open("./files/name.txt", "w" , encoding="utf-8") as f:
        for name in names:
            f.write(name)
            f.write('\n')

def add_name(name):
    """_This function allows you to add a name to a file and do some more things to be useful_
    """
    with open("./files/name.txt", "a" , encoding="utf-8") as f:
        f.write(name)
        f.write("\n")

def delete_name(name):
    """_This function allows you to delete a name to a file and do some more things to be useful_
    """
    with open("./files/name.txt", "r", encoding="utf-8") as f:
        for line in f:
            if len(line.strip()) > 0 and line.strip()!= name:
                names.append(line.strip())
    with open("./files/name.txt", "w" , encoding="utf-8") as f:
        for name in names:
            f.write(name)
            f.write('\n')

def run():
    op = True
    while op:
        try:
            print("""
----------------------------------------------------------------------
            Seleccione un numero:
            1. Create a mew file
            2. Add name
            3. List name(s)
            4. Delete name
            5. Exit
----------------------------------------------------------------------
            """)
            n = int(input("Enter an option :   "))
            if n == 1:
                write()
            elif n == 2:
                name = input("Enter a name to add : ")
                add_name(name)
            elif n == 3:
                read()
            elif n == 4:
                name = input("Enter a name to delete : ")
                delete_name(name)
            elif n ==5:
                op = False
                print("Program Finished!")
        except ValueError :
                print("Error!!! Please select a valid option!")

if __name__ == '__main__':
    run()