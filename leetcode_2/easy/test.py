def test(string):
    if not string:
        return -1, 0

    max_l = 1
    index = 0
    curr = 0
    count = 1
    for i in range(len(string) - 1):
        if string[i] == string[i + 1]:
            if count == 1:
                curr = i
            count += 1
        else:
            if count > max_l:
                max_l = count
                index = curr

            count = 1

    if count > max_l:
        max_l = count
        index = curr

    return index, max_l


s = 'djdjdjdggggffaaaaaaaaaa'
print(test(s))
