from math import sqrt


def square(n):
    return square_helper(n, 1, n)


def square_helper(n, min, max):
    if max < min:
        return -1

    guess = (min + max) // 2
    guess_p2 = guess * guess
    if guess_p2 == n:
        return guess
    elif guess_p2 > n:
        return square_helper(n, min, guess - 1)
    else:
        return square_helper(n, guess + 1, max)


def square_finding(n):
    for i in range(1, int(sqrt(n)) + 1):
        if i * i == n:
            return i

    return -1


print(square_finding(9))
a = square(9)
print(a)
