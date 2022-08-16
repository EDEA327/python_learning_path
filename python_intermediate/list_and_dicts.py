def run():
    # my_list = [1,'Hello',True,4.5]
    # my_dict = {'Firstname': 'Erick', 'Lastname':'Escobar'}

    super_list = [
        {'Firstname': 'Erick', 'Lastname':'Escobar'},
        {'Firstname': 'Daniel', 'Lastname':'Tejeda'},
        {'Firstname': 'Edber', 'Lastname':'Taboada'},
        {'Firstname': 'Daniel', 'Lastname':'Anzoategui'},
        {'Firstname': 'Alejandro', 'Lastname':'Castellón'}
    ]

    super_dict = {
        "natural_nums":[1,2,3,4,5],
        "integer_nums":[-1,-2,0,1,2],
        "float_nums":[1.2,2.3,3.4,4.5,5.6]
    }

    for k,v in super_dict.items():
        print (k, "-", v)
    for element in super_list:
        print (element['Firstname'], "-" , element['Lastname'])


if __name__ == '__main__':
    run()