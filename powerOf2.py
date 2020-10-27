def powerOf2(n):
    if n < 1:
        return 0
    elif n == 1:
        print(1)
        return 1
    else:
        prev = powerOf2(n // 2)
        current = prev * 2
        print(current)
        return current


powerOf2(5)
