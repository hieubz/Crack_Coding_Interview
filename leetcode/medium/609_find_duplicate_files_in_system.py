# given a list of directory path, and all the files with contents in this director
# you need to find out all the groups of duplicate files in the file system in terms of their contents


class Solution:
    def findDuplicate(self, paths):
        dicts = {}
        for path in paths:
            files = path.split(' ')
            for file in files[1:]:
                file_name, content = file.split('(')
                content = content[:-1]
                if content not in dicts:
                    dicts[content] = [files[0] + '/' + file_name]
                else:
                    dicts[content].append(files[0] + '/' + file_name)

        result = []
        for k, v in dicts.items():
            if len(v) > 1:
                result.append(v)

        return result


# Follow up
# 1 Imagine you are given a real file system, how will you search files? DFS or BFS?
# 2. If the file content is very large (GB level), how will you modify your solution?
# 3. IF you can only read the file by 1kb each time, how will you modify your solution?
# 4. What is the time complexity of your modified solution? What is the most time-consuming part and memory
# consuming part of it? How to optimize?
# 5. How to make sure the duplicated files you find are not false positive?


# Answers
# 1. In general, BFS will use more memory than DFS. However BFS can take advantage of the locality of files
# inside directories, and therefore will probably be faster
# 2. in this case, not realistic to match the whole string of the content. So we use file size
# map all the files according to size. Files with different sizes are guaranteed to be different
# Then we hash a small part of the files with equal sizes (using MD5 for example). Only if the MD5 is
# the same, we will compare the files byte by byte
# 3. we can create the hash from the 1kb chunks and then read the entire file if a full byte by byte comparison
# is required
# 4. O(n^2 * k) since in worse case we might meed to compare every file to all others.
# 5. use some filters like file size, hash a small part


s = Solution()
res = s.findDuplicate(["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"])
print(res)