def check(s1, s2):
    """check if they are one edit or zero edit away"""

    l1 = len(s1)
    l2 = len(s2)

    if len(s1) == len(s2):
        return check_update(s1, s2)
    elif l1 + 1 == l2:
        return check_insert(s1, s2)
    elif l1 - 1 == l2:
        return check_insert(s2, s1)
    else:
        return False


def check_update(s1, s2):
    count_update = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            count_update += 1
            if count_update > 1:
                return False

    return True


def check_insert(s1, s2):
    count_insert = 0
    index1 = 0
    index2 = 0
    while index1 < len(s1):
        if s1[index1] != s2[index2]:

            index2 += 1
        else:
            index1 += 1
            index2 += 1

    return True


print(check('apple', 'aple'))
