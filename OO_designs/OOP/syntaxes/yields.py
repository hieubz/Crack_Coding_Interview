"""
Return sends a specified value back to its caller and terminates a function entirely
whereas yield can produce a sequence of values
1. generators are used to create iterators
create a generator: create a normal function with a yield statement.
"""


def rev_str_2(my_str):
    length = len(my_str)
    for i in range(length):
        yield my_str[i]


for char in rev_str_2("fuck"):
    print(char)
