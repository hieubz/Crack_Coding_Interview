def replace_spaces(string):

    string = string.strip()
    true_length = len(string)
    count_spaces = string.count(' ')
    new_length = true_length + count_spaces * 2

    string = list(string)
    for f in range(true_length, new_length):
        string.append('0')

    index = new_length - 1
 
    for j in range(true_length - 1, 0, -1):
        if string[j] != ' ':
            string[index] = string[j]
            index -= 1
        else:
            string[index] = '0'
            string[index - 1] = '2'
            string[index - 2] = '%'
            index -= 3

    return ''.join(string)


if __name__ == '__main__':
    s = "Mr John Smith "
    s = replace_spaces(s)
    print(s)
