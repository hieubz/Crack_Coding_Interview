import unittest


class Book:
    def __init__(self, text):
        self.text = text


class BookReader:
    def __init__(self, books):
        self.books = books

    def read_next_book(self):
        if len(self.books):
            return self.books.pop(0).text
        else:
            return None


class Test(unittest.TestCase):
    def test_online_book_reader(self):
        reader = BookReader([Book("the start."), Book("The end.")])
        self.assertEqual(reader.read_next_book(), "the start.")
        self.assertEqual(reader.read_next_book(), "The end.")
        self.assertEqual(reader.read_next_book(), None)


if __name__ == '__main__':
    unittest.main()