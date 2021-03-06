class Solution:
    def findDuplicate(self, paths):
        dict = {}
        for element in paths:
            arr_spl = element.split(" ")
            for file in arr_spl[1:]:
                split_file = file.split("(")
                f_name, content = split_file[0], split_file[1][:-1]
                if content not in dict:
                    dict[content] = [arr_spl[0] + '/' + f_name]
                else:
                    dict[content].append(arr_spl[0] + '/' + f_name)

        result = []
        for value in dict.values():
            if len(value) > 1:
                result.append(value)

        return result
