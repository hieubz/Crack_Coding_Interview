from itertools import permutations
from print_all_permutation import Tools


def find_permutation(s: str, b: str):
    """
    find all permutation of s in b and return the index of these
    :param s:
    :param b:
    :return:
    """

    chars_in_s = set(s)
    list_str = list(s)

    tools = Tools()

    # O(n!)
    permutation_s = tools.permute(list_str, 0, len(list_str))
    # permutation_s = permutations(s, len(s))

    # O(n)
    for i in range(0, len(b) - 3):
        if b[i] in chars_in_s:
            if b[i:(i + 4)] in permutation_s:
                print(i)

    # => O(n! + n)
