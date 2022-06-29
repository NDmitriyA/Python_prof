class MeIterator:

    def __init__(self, list_):
        self._list = list_
        self.cursor = 0
        self.nest_cursor = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.cursor < len(self._list):
            if self.nest_cursor < len(self._list[self.cursor]):
                lst = self._list[self.cursor][self.nest_cursor]
                self.nest_cursor += 1
                return lst
            self.cursor += 1
            self.nest_cursor = 0
        raise StopIteration


def main():
    nested_list = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None],
    ]
    for item in MeIterator(nested_list):
        print(item)
    print('----------')
    flat_list = [item for item in MeIterator(nested_list)]
    print(flat_list)


main()
