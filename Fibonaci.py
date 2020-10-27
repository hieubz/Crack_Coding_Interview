def fib(n: int):
    if n < 0:
        return 0
    elif n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


print(fib(3))


def fib_memo(n: int, memo):
    if n <= 0:
        return 0
    elif n == 1:
        return 1 
    elif n < len(memo):
        return memo[n]

    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)

    return memo[n]


memo = {}
print(fib_memo(3, memo))
