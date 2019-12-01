import time
from timeit import Timer

"""
timer decorator 
함수의 실행시간을 time 모듈을 이용해 측정한다.
functools.wraps는 데코레이트 된 함수의 정체성을 유지시킨다.
@wraps가 없을 경우: function.__name__ => inner
@wraps가 있을 경우: function.__name__ => function
"""


def benchmarker_time(org_func):
    # @wraps(org_func)
    def inner(*args, **kwargs):
        start = time.time()
        result = org_func(*args, **kwargs)
        elapsed = time.time() - start
        print(f'elapsed time with timer decorator : {elapsed:.2f}')
        return result

    return inner


@benchmarker_time
def function(n):
    for i in range(n):
        n += i
    return n


function(1000000)

"""
timeit 모듈을 이용한 간편 구조
아래의 구조를 이용해 함수의 실행 시간을 측정한다.

t = Timer('function(arg)', 'from __main__ import function')
t.timeit() 
"""


def number_sum(n):
    if n == 0:
        return 0
    else:
        return n + number_sum(n - 1)


t = Timer('number_sum(30)', 'from __main__ import number_sum')
print(f'elapsed time with timeit: {t.timeit():.2f}')
