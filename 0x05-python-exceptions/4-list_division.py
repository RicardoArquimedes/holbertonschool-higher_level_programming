#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    x = []
    for y in range(list_length):
        try:
            x.append(my_list_1[y] / my_list_2[y])
        except TypeError:
            x.append(0)
            print("wrong type")
        except ZeroDivisionError:
            x.append(0)
            print("division by 0")
        except IndexError:
            x.append(0)
            print("out of range")
        finally:
            pass
    return x
