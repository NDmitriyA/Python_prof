from datetime import datetime
import os


def decor_fun(func):
    CACHE_TIME = {}

    def time_date_func(*args, **kwargs):
        tm = str(datetime.now().time())
        dt = str(datetime.now().date())
        CACHE_TIME["date"] = dt
        CACHE_TIME["time"] = tm
        CACHE_TIME["name function"] = func.__name__
        CACHE_TIME["log"] = os.getcwd()
        CACHE_TIME["start"] = func(*args, **kwargs)
        CACHE_TIME["stop"] = func(*args, **kwargs)
        with open('log_list_func.json', 'w') as f:
            f.write(str(CACHE_TIME))

    return time_date_func


# @decor_fun
# def sum_test_decor(a: int, b: int) -> int:
#     return a * b
#
#
# sum_test_decor(6, 7)
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

@decor_fun
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
