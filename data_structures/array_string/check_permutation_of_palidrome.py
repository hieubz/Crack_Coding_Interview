def check(string):
    dicts = {}
    for s in string:
        if s not in dicts:
            dicts[s] = 1
        else:
            dicts[s] += 1

    count = 0
    for k, v in dicts.items():
        if v % 2 == 1:
            count += 1
            if count > 1:
                return False

    return True


print(check('baocaosu'))
