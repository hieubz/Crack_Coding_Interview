def sum_digits(n):
    sums: int = 0
    while n > 0:
        sums += n % 10
        n = n // 10

    return sums


print(sum_digits(35)) 
