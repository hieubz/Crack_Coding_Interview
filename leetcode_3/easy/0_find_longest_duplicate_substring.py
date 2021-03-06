def find(string):
    result = {
        "start": 0,
        "length": 1
    }

    current = {
        "start": 0,
        "length": 1
    }

    for i in range(len(string) - 1):
        if string[i] == string[i + 1]:
            current["length"] += 1
        else:
            current["start"] = i + 1
            current["length"] = 1

        if current["length"] > result["length"]:
            result = current.copy()

    print(result)

    return string[result["start"]:result["start"] + result["length"]]


if __name__ == '__main__':
    s = "abbbbbcccccccccdddxxxxxxxzzzzysssaabbcccddeeffffffffffffff"
    print(find(s))
