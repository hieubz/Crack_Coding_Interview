# 1st

# O(n4)
def normal_way(n):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            for c in range(1, n + 1):
                for d in range(1, n + 1):
                    if pow(a, 3) + pow(b, 3) == pow(c, 3) + pow(d, 3):
                        print(a, b, c, d)
                        break


# O(n3)
def first_improve(n):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            for c in range(1, n + 1):
                d = int(pow(pow(a, 3) + pow(b, 3) - pow(c, 3), 1 / 3))
                if pow(a, 3) + pow(b, 3) == pow(c, 3) + pow(d, 3):
                    print(a, b, c, d)


# O(n2)
def best_solution(n, dicts):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            result = pow(a, 3) + pow(b, 3)
            if result in dicts:
                dicts[result].append((a, b))
            else:
                dicts[result] = [(a, b)]

    for result, pairs in dicts.items():
        for pair in pairs:
            for pair_2 in pairs:
                print(pair, pair_2)


best_solution(100, {})
