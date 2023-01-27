#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    idx = 0
    try:
        for i in my_list:
            if x > idx:
                print("{}".format(my_list[idx]), end="")
                idx = idx + 1
        print()
    except TypeError:
        pass
    finally:
        return(idx)
