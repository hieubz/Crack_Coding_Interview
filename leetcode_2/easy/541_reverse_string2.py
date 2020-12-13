def reverseStr(s: str, k: int) -> str:
    len_s = len(s)
    s = list(s)
    num = len_s // k
    last_part = len_s % k
    for i in range(1, num, 2):
        s[((i - 1) * k):(i * k)] = list(s[((i - 1) * k):(i * k)])[::-1]

    if last_part > k:
        s[(len_s - last_part):-(last_part - k)] = s[(len_s - last_part):-(last_part - k)][::-1]
    else:
        if num % 2 == 0:
            s[(num * k):] = s[(num * k):][::-1]

    return ''.join(s)


def reverse2(s, k):
    len_s = len(s)
    s = list(s)

    for i in range(0, len_s, 2 * k):
        s[i:(i + k)] = s[i:(i + k)][::-1]

    return ''.join(s)


reverse2("abcdabcdfd", 4)
