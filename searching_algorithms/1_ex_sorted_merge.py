

def merge_3(arr1, arr2):
    i = len(arr1) - 1
    j = len(arr2) - 1
    arr1 += [0] * (j + 1)
    k = i + j + 1

    while i >= 0 and j >= 0:
        if arr1[i] > arr2[j]:
            arr1[k] = arr1[i]
            i -= 1
        else:
            arr1[k] = arr2[j]
            j -= 1

        k -= 1

    while j >= 0:
        arr1[k] = arr2[j]
        k -= 1
        j -= 1

    return arr1
