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


@decor_fun
def sum_test_decor(a: int, b: int) -> int:
    return a * b


sum_test_decor(6, 7)

