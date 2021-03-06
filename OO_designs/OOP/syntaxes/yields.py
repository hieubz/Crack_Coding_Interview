"""
Return sends a specified value back to its caller and terminates a function entirely
whereas yield can produce a sequence of values
1. generators are used to create iterators
create a generator: create a normal function with a yield statement.
"""


def rev_str(my_str):
    length = len(my_str)
    for i in range(length - 1, -1, -1):
        yield my_str[i]


for c in rev_str("fuck"):
    print(c)
