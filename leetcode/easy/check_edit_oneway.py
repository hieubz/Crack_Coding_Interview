def is_one_edit(str_1, str_2):
    if str_1 == str_2:
        return True

    len_1 = len(str_1)
    len_2 = len(str_2)

    # diff length
    if abs(len_1 - len_2) > 1:
        return False

    i = 0
    j = 0
    diff = 0

    # check diff by each character
    while i < len_1 and j < len_2:
        f = str_1[i]
        s = str_2[j]
        if f != s:
            diff += 1
            # insert or remove
            if len_1 > len_2:
                i += 1
            elif len_2 > len_1:
                j += 1
            else:
                # replace
                i += 1
                j += 1
        else:
            i += 1
            j += 1

        if diff > 1:
            return False

    # if diff == 1 and len_1 != len_2 and (i != len_1 or j != len_2):
    #     return False

    return True


is_one_edit('pale', 'bale')
