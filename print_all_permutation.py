class Tools:
    def __init__(self):
        self.permutation_arr = {}

    @staticmethod
    def to_string(list_chars):
        return ''.join(list_chars)

    # O(n!)
    def permute(self, string, l, r):
        if l == r:
            self.permutation_arr[(self.to_string(string))] = 1
        else:
            for step in range(l, r + 1):
                string[l], string[step] = string[step], string[l]
                self.permute(string, l + 1, r)
                string[l], string[step] = string[step], string[l]  # backtrack


strings = 'ABC'
leng = len(strings)
arr = list(strings)
tools = Tools()
tools.permute(arr, 0, leng - 1)
print(tools.permutation_arr)
