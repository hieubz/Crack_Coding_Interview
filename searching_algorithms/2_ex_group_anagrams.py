# write a method to sort an array of strings so that all the anagrams are next to each other

def group_anagrams(arr):
    dicts = {}
    for s in arr:
        sorted_s = str(sorted(s))
        if sorted_s not in dicts:
            dicts[sorted_s] = [s]
        else:
            dicts[sorted_s].append(s)

    i = 0
    arr = []
    for k in dicts.keys():
        arr += dicts[k]

    return arr


arr = ['ab', 'cc', 'ba', 'cc']
print(group_anagrams(arr))