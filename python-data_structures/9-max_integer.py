#!/usr/bin/python3
def max_integer(my_list=[]):
    max = my_list[0]
    if not(my_list):
        return None
    for i in (my_list):
        if(max < i):
            max = i
            return(max)

