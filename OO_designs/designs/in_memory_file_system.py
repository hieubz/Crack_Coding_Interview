# design an in-memory file system
# 1. making a list of the key objects in the system, then think about how they interact
# 2. what is the relationship between the file and directory?
import unittest


class Directory:
    def __init__(self, name):
        self.name = name
        self.parent = None
        self.files = {}
        self.sub_dirs = {}

    def add_sub_dir(self, directory):
        # delete directory in its old parent
        if directory.parent:
            del directory.parent.sub_dirs[directory.name]

        # reassign it to the directory
        directory.parent = self
        # add it to sub directories list
        self.sub_dirs[directory.name] = directory

    def add_file(self, file):
        self.files[file.name] = file

    def get(self, path):
        """
        get sub elements of current dir by path
        :param path:
        :return:
        """
        parts = path.split('/')
        directory = self
        for part in parts:
            # check ".." notation
            if part == "..":
                directory = directory.parent
                # no parent
                if not directory:
                    return None
            elif part in directory.sub_dirs:
                # check sub dirs
                directory = directory.sub_dirs[part]
            elif part in directory.files:
                # check child files
                return directory.files[part]

        # if cannot return anything => return the current directory

        return directory


class File:
    def __init__(self, name, content):
        self.name, self.content = name, content


class Test(unittest.TestCase):
    def test_file_system(self):
        dir_1 = Directory('root')
        dir_2 = Directory('hieu')
        dir_3 = Directory('my_girl')

        file_1 = File('new_plan.txt', "let me try")
        dir_1.add_sub_dir(dir_2)
        dir_2.add_sub_dir(dir_3)
        dir_3.add_file(file_1)

        self.assertEqual(dir_1.get('root/hieu/my_girl/new_plan.txt'), file_1)


if __name__ == '__main__':
    unittest.main()


