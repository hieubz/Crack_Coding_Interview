def compress(string):
    len_s = len(string)
    final_length = check_compress_length(string)
    if final_length > len_s:
        return string

    compress_str = ''
    count_duplicate = 0
    for i in range(len_s):
        count_duplicate += 1
        if i == len_s - 1 or string[i] != string[i + 1]:
            compress_str += string[i]
            compress_str += str(count_duplicate)
            count_duplicate = 0

    return compress_str


def check_compress_length(string):
    len_s = len(string)

    compress_len = 0
    count_duplicate = 0
    for i in range(len_s):
        count_duplicate += 1
        if i == len_s - 1 or string[i] != string[i + 1]:
            compress_len += 1 + 1 if count_duplicate > 0 else 0
            count_duplicate = 0

    return compress_len


print(compress('aabbcccwwwwwaa'))
