nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    [1, 2, None],
]


def gen(nl):
    for l in nl:
        for i in l:
            yield i


for item in gen(nested_list):
    print(item)
