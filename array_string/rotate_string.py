
def check_rotate_string(s1, s2):
    length = len(s1)

    if length == len(s2) and length > 0:
        new_str = s2 + s2
        return is_substring(new_str, s1)

    return False


def is_substring(s1, s2):
    if s2 in s1:
        return True

    return False
