def make_division_by(n):
    """Make a division by n. using closures
    Note : A closure occurs when 3 rules are met.
    1- There is a nested superior scope function
    2- the nested function references variables of a higher scope
    3- The nested function is returned."""
    def division(s):
        return s / n
    return division
def run():
    division_by_3 = make_division_by(3)
    division_by_4 = make_division_by(4)
    division_by_5 = make_division_by(5)
    division_by_6 = make_division_by(6)
    print(division_by_3(9))
    print(division_by_4(16))
    print(division_by_5(25))
    print(division_by_6(36))
if __name__ == '__main__':
    run()
