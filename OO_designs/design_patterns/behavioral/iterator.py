"""
provide a way to access the elements of an object sequentially without exposing its underlying representation (list, array)
elements are stored in data structures in some different ways so when you need to iterate through them,
 you need to implement many different loops - duplicated code
 => we have iterator pattern for this to implement an interface for them
"""

from __future__ import annotations
from collections.abc import Iterable, Iterator
from typing import Any, List


class AlphabeticalOrderIterator(Iterator):
    _position = None
    _reverse = False

    def __init__(self, collection, reverse):
        self._collection = collection
        self._reverse = reverse
        self._position = -1 if reverse else 0

    def __next__(self):
        try:
            value = self._collection[self._position]
            self._position += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration

        return value


class WordsCollection(Iterable):
    """
    concrete collection
    """

    def __init__(self, words_list: List[Any] = []) -> None:
        self.words_list = words_list

    def __iter__(self):
        return AlphabeticalOrderIterator(self.words_list, False)

    def get_reverse_iterator(self) -> Iterator:
        return AlphabeticalOrderIterator(self.words_list, True)

    def add_item(self, item: Any):
        self.words_list.append(item)

    def print_elements(self, iterator):
        while iterator.has_next():
            print(iterator.__next__())


if __name__ == '__main__':
    collection = WordsCollection()
    collection.add_item('1')
    collection.add_item('2')

    print(' '.join(collection))
    print(' '.join(collection.get_reverse_iterator()))




